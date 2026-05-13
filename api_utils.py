"""
API Utilities Module
Handles all external API calls with proper error handling and caching
"""

import aiohttp
import logging
import asyncio
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Any
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timezone
import io

import config
from cache import get_cache, get_rate_limiter, cache_key

logger = logging.getLogger(__name__)


# ============================================================================
# COINGECKO API - PRICE CHARTS
# ============================================================================

async def fetch_price_chart(
    coin_id: str,
    vs_currency: str = "usd",
    days: int = 1,
    use_cache: bool = True
) -> Optional[io.BytesIO]:
    """
    Fetch 24h price chart for a cryptocurrency
    
    Args:
        coin_id: CoinGecko coin ID (e.g., 'bitcoin')
        vs_currency: Target currency (default: 'usd')
        days: Number of days of data (default: 1 for 24h)
        use_cache: Use in-memory cache (default: True)
    
    Returns:
        BytesIO object containing PNG chart data
    """
    
    # Check cache first
    cache_key_str = cache_key(coin_id, vs_currency)
    if use_cache:
        cached = get_cache().get(cache_key_str)
        if cached:
            logger.info(f"📊 Using cached chart for {coin_id}")
            return cached
    
    try:
        # Rate limiting
        limiter = get_rate_limiter()
        await limiter.wait_if_needed()
        
        # Fetch data
        url = (
            f"{config.COINGECKO_API_BASE}/coins/{coin_id}/market_chart"
            f"?vs_currency={vs_currency}&days={days}"
        )
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=config.COINGECKO_TIMEOUT) as resp:
                if resp.status != 200:
                    logger.error(f"❌ CoinGecko API error: {resp.status}")
                    return None
                
                data = await resp.json()
        
        prices = data.get("prices", [])
        if not prices:
            logger.warning(f"⚠️ No price data for {coin_id}")
            return None
        
        # Generate chart
        chart = _generate_chart(coin_id, prices)
        
        # Cache the chart
        if use_cache:
            get_cache().set(cache_key_str, chart)
        
        return chart
    
    except asyncio.TimeoutError:
        logger.error(f"⏱️ Timeout fetching chart for {coin_id}")
        return None
    except Exception as e:
        logger.error(f"❌ Chart fetch error for {coin_id}: {e}")
        return None


def _generate_chart(coin_name: str, prices: List[List[float]]) -> io.BytesIO:
    """
    Generate matplotlib chart from price data
    
    Args:
        coin_name: Coin name/ID for title
        prices: List of [timestamp, price] pairs
    
    Returns:
        BytesIO object containing PNG chart
    """
    
    try:
        # Parse data
        times = [
            datetime.fromtimestamp(p[0] / 1000.0, tz=timezone.utc)
            for p in prices
        ]
        values = [p[1] for p in prices]
        
        # Determine trend (green for up, red for down)
        is_up = values[-1] >= values[0]
        color = config.COLORS["success"] if is_up else config.COLORS["danger"]
        trend_emoji = "📈" if is_up else "📉"
        
        # Create figure with professional styling
        fig, ax = plt.subplots(figsize=(10, 5), facecolor=config.COLORS["dark"])
        ax.set_facecolor(config.COLORS["dark"])
        
        # Plot line and fill
        ax.plot(times, values, color=color, linewidth=2.5, label="Price")
        ax.fill_between(
            times, values, min(values) * 0.99,
            color=color, alpha=0.15, label="Area"
        )
        
        # Styling
        title = f"{coin_name.upper()} - 24h Price Chart {trend_emoji}"
        ax.set_title(title, color="white", pad=20, fontsize=14, fontweight="bold")
        ax.grid(True, color="#333333", linestyle="--", alpha=0.4)
        
        # Axis styling
        ax.tick_params(colors="#888888", which="both", labelsize=9)
        for spine in ax.spines.values():
            spine.set_color("#444444")
            spine.set_linewidth(0.5)
        
        # Format x-axis
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
        
        # Add legend
        ax.legend(loc="upper left", facecolor=config.COLORS["dark"], 
                 edgecolor="#555555", labelcolor="white")
        
        # Save to buffer
        buf = io.BytesIO()
        plt.savefig(
            buf, format="png", bbox_inches="tight", dpi=100,
            facecolor=config.COLORS["dark"], edgecolor="none"
        )
        buf.seek(0)
        plt.close("all")
        
        logger.info(f"✅ Chart generated for {coin_name}")
        return buf
    
    except Exception as e:
        logger.error(f"❌ Chart generation error: {e}")
        plt.close("all")
        return None


# ============================================================================
# COINGECKO API - PRICE DATA
# ============================================================================

async def fetch_price_data(coin_id: str, vs_currency: str = "usd") -> Optional[Dict[str, Any]]:
    """
    Fetch current price and market data for a coin
    
    Args:
        coin_id: CoinGecko coin ID
        vs_currency: Target currency
    
    Returns:
        Dict with price, market_cap, volume, change, etc.
    """
    
    try:
        # Rate limiting
        limiter = get_rate_limiter()
        await limiter.wait_if_needed()
        
        url = (
            f"{config.COINGECKO_API_BASE}/coins/markets"
            f"?vs_currency={vs_currency}&ids={coin_id}"
            f"&order=market_cap_desc&per_page=1"
        )
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=config.COINGECKO_TIMEOUT) as resp:
                if resp.status != 200:
                    logger.error(f"❌ Price API error: {resp.status}")
                    return None
                
                data = await resp.json()
                if data:
                    logger.debug(f"✅ Price data fetched for {coin_id}")
                    return data[0]
        
        return None
    
    except asyncio.TimeoutError:
        logger.error(f"⏱️ Timeout fetching price for {coin_id}")
        return None
    except Exception as e:
        logger.error(f"❌ Price fetch error: {e}")
        return None


# ============================================================================
# COINDESK API - NEWS
# ============================================================================

async def fetch_crypto_news(limit: int = 5) -> List[Dict[str, str]]:
    """
    Fetch latest crypto news from CoinDesk RSS feed
    
    Args:
        limit: Maximum number of articles to fetch
    
    Returns:
        List of dicts with 'title' and 'link'
    """
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                config.COINDESK_NEWS_URL,
                timeout=config.COINDESK_TIMEOUT
            ) as resp:
                if resp.status != 200:
                    logger.error(f"❌ News API error: {resp.status}")
                    return []
                
                content = await resp.read()
        
        # Parse RSS
        root = ET.fromstring(content)
        news = []
        
        for item in root.findall(".//item")[:limit]:
            title = item.findtext("title", default="Untitled")
            link = item.findtext("link", default="")
            
            if title and link:
                news.append({
                    "title": title.strip(),
                    "link": link.strip(),
                    "source": "CoinDesk"
                })
        
        logger.info(f"✅ Fetched {len(news)} news articles")
        return news
    
    except asyncio.TimeoutError:
        logger.error("⏱️ Timeout fetching news")
        return []
    except Exception as e:
        logger.error(f"❌ News fetch error: {e}")
        return []


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def format_large_number(num: float) -> str:
    """Format large numbers with readable units"""
    if num is None or num == 0:
        return "N/A"
    
    if num >= 1_000_000_000_000:
        return f"${num / 1_000_000_000_000:.2f}T"
    elif num >= 1_000_000_000:
        return f"${num / 1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"${num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"${num / 1_000:,.2f}K"
    else:
        return f"${num:,.2f}"


def format_price(price: float, symbol: str = "$") -> str:
    """Format price with appropriate decimal places"""
    if price is None:
        return "N/A"
    
    if price >= 1:
        return f"{symbol}{price:,.2f}"
    else:
        # Show more decimals for small prices
        return f"{symbol}{price:.8f}".rstrip("0").rstrip(".")


def get_trend_emoji(change: Optional[float]) -> str:
    """Get emoji based on percentage change"""
    if change is None:
        return "➡️"
    elif change > 0:
        return "📈"
    elif change < 0:
        return "📉"
    else:
        return "➡️"