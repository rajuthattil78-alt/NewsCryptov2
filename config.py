"""
Configuration & Constants
Professional Crypto Trading Bot
"""

import os
from typing import Dict, List

# ============================================================================
# BOT CONFIG
# ============================================================================
BOT_TOKEN = "8"
BOT_NAME = "CryptoHub Pro"

# ============================================================================
# REDIS CONFIG (FOR REAL-TIME PRICES)
# ============================================================================
REDIS_URL = "redis://localhost:6379/0"
REDIS_PRICE_KEY = "market_prices"

# ============================================================================
# API ENDPOINTS & TIMEOUTS
# ============================================================================
COINGECKO_API_BASE = "https://api.coingecko.com/api/v3"
COINGECKO_TIMEOUT = 15  # seconds
COINGECKO_CHART_DAYS = 1  # 24-hour chart

COINDESK_NEWS_URL = "https://www.coindesk.com/arc/outboundfeeds/rss/"
COINDESK_TIMEOUT = 15
COINDESK_NEWS_LIMIT = 5

# ============================================================================
# CACHE CONFIG
# ============================================================================
CHART_CACHE_TTL = 600  # Update every 10 minutes (600 seconds)
MAX_CHART_CACHE_SIZE = 50  # Keep cache for max 50 coins

# ============================================================================
# DATABASE CONFIG
# ============================================================================
DB_FILE_NAME = "data.json"

# ============================================================================
# SUPPORTED CRYPTOCURRENCIES
# ============================================================================
SUPPORTED_COINS: Dict[str, Dict[str, str]] = {
    "BTC": {"id": "bitcoin", "name": "Bitcoin", "emoji": "₿"},
    "ETH": {"id": "ethereum", "name": "Ethereum", "emoji": "Ξ"},
    "USDT": {"id": "tether", "name": "Tether", "emoji": "₮"},
    "SOL": {"id": "solana", "name": "Solana", "emoji": "◎"},
    "BNB": {"id": "binancecoin", "name": "BNB", "emoji": "⬟"},
    "XRP": {"id": "ripple", "name": "XRP", "emoji": "✕"},
    "TON": {"id": "the-open-network", "name": "Toncoin", "emoji": "◆"},
    "DOGE": {"id": "dogecoin", "name": "Dogecoin", "emoji": "Ð"},
    "ADA": {"id": "cardano", "name": "Cardano", "emoji": "₳"},
    "TRX": {"id": "tron", "name": "TRON", "emoji": "T"},
    "AVAX": {"id": "avalanche-2", "name": "Avalanche", "emoji": "▲"},
    "LINK": {"id": "chainlink", "name": "Chainlink", "emoji": "🔗"},
    "DOT": {"id": "polkadot", "name": "Polkadot", "emoji": "●"},
    "MATIC": {"id": "polygon-ecosystem-token", "name": "Polygon", "emoji": "◈"},
    "LTC": {"id": "litecoin", "name": "Litecoin", "emoji": "Ł"},
}

# ============================================================================
# FIAT CURRENCIES
# ============================================================================
SUPPORTED_FIATS: Dict[str, Dict[str, str]] = {
    "usd": {"name": "US Dollar", "symbol": "$", "flag": "🇺🇸"},
    "eur": {"name": "Euro", "symbol": "€", "flag": "🇪🇺"},
    "inr": {"name": "Indian Rupee", "symbol": "₹", "flag": "🇮🇳"},
    "gbp": {"name": "British Pound", "symbol": "£", "flag": "🇬🇧"},
    "aed": {"name": "UAE Dirham", "symbol": "د.إ", "flag": "🇦🇪"},
    "jpy": {"name": "Japanese Yen", "symbol": "¥", "flag": "🇯🇵"},
    "cad": {"name": "Canadian Dollar", "symbol": "C$", "flag": "🇨🇦"},
    "aud": {"name": "Australian Dollar", "symbol": "A$", "flag": "🇦🇺"},
    "chf": {"name": "Swiss Franc", "symbol": "CHF", "flag": "🇨🇭"},
    "cny": {"name": "Chinese Yuan", "symbol": "¥", "flag": "🇨🇳"},
    "krw": {"name": "South Korean Won", "symbol": "₩", "flag": "🇰🇷"},
    "mxn": {"name": "Mexican Peso", "symbol": "Mex$", "flag": "🇲🇽"},
}

# ============================================================================
# COLORS FOR UI (HEX CODES FOR CONSISTENCY)
# ============================================================================
COLORS = {
    "primary": "#1f77e7",      # Professional Blue
    "success": "#2ecc71",       # Green (for gains)
    "danger": "#e74c3c",        # Red (for losses)
    "warning": "#f39c12",       # Orange (for alerts)
    "dark": "#1e1e1e",          # Dark background
    "light": "#ecf0f1",         # Light text
}

# ============================================================================
# CHAT ACTIONS
# ============================================================================
CHAT_ACTIONS = {
    "typing": "typing",
    "upload_photo": "upload_photo",
    "upload_document": "upload_document",
    "find_location": "find_location",
}

# ============================================================================
# LOGGING
# ============================================================================
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"