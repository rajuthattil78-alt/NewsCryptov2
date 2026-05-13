"""
In-Memory Cache Manager
Handles chart data caching with TTL (Time-To-Live)
Prevents API rate limiting by caching for 10 minutes
"""

import io
import time
import logging
from typing import Dict, Optional, Tuple
from datetime import datetime, timedelta
import asyncio

logger = logging.getLogger(__name__)


class CacheEntry:
    """Represents a cached item with TTL"""
    
    def __init__(self, data: io.BytesIO, ttl_seconds: int = 600):
        self.data = data
        self.created_at = time.time()
        self.ttl = ttl_seconds
    
    def is_expired(self) -> bool:
        """Check if cache entry has expired"""
        return (time.time() - self.created_at) > self.ttl
    
    def get_age_seconds(self) -> int:
        """Get age of cache entry in seconds"""
        return int(time.time() - self.created_at)


class ChartCache:
    """
    In-memory chart cache with LRU eviction
    Stores generated price charts to avoid repeated API calls
    """
    
    def __init__(self, max_entries: int = 50, ttl_seconds: int = 600):
        self.cache: Dict[str, CacheEntry] = {}
        self.max_entries = max_entries
        self.ttl_seconds = ttl_seconds
        self.hits = 0
        self.misses = 0
    
    def set(self, key: str, data: io.BytesIO) -> None:
        """Store chart in cache"""
        # Remove old entries if cache is full
        if len(self.cache) >= self.max_entries:
            self._evict_oldest()
        
        self.cache[key] = CacheEntry(data, self.ttl_seconds)
        logger.debug(f"📊 Chart cached: {key}")
    
    def get(self, key: str) -> Optional[io.BytesIO]:
        """
        Retrieve chart from cache if valid
        Returns: BytesIO object or None if expired/not found
        """
        if key not in self.cache:
            self.misses += 1
            return None
        
        entry = self.cache[key]
        
        # Check if expired
        if entry.is_expired():
            del self.cache[key]
            self.misses += 1
            logger.debug(f"♻️ Cache expired: {key}")
            return None
        
        # Reset file pointer for reading
        entry.data.seek(0)
        self.hits += 1
        logger.debug(f"✅ Cache hit: {key} (age: {entry.get_age_seconds()}s)")
        return entry.data
    
    def _evict_oldest(self) -> None:
        """Remove oldest entry from cache (LRU)"""
        if not self.cache:
            return
        
        oldest_key = min(
            self.cache.keys(),
            key=lambda k: self.cache[k].created_at
        )
        
        del self.cache[oldest_key]
        logger.debug(f"🗑️ Evicted: {oldest_key}")
    
    def clear(self) -> None:
        """Clear all cache entries"""
        self.cache.clear()
        logger.info("🧹 Cache cleared")
    
    def get_stats(self) -> Dict[str, any]:
        """Get cache statistics"""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "entries": len(self.cache),
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.1f}%",
            "max_size": self.max_entries
        }
    
    def get_entry_status(self, key: str) -> Optional[Dict[str, any]]:
        """Get detailed status of a cache entry"""
        if key not in self.cache:
            return None
        
        entry = self.cache[key]
        return {
            "age_seconds": entry.get_age_seconds(),
            "ttl_seconds": entry.ttl,
            "is_expired": entry.is_expired(),
            "remaining_seconds": max(0, entry.ttl - entry.get_age_seconds())
        }


# Global cache instance
_chart_cache: Optional[ChartCache] = None


def init_cache(max_entries: int = 50, ttl_seconds: int = 600) -> ChartCache:
    """Initialize the global chart cache"""
    global _chart_cache
    _chart_cache = ChartCache(max_entries, ttl_seconds)
    logger.info(f"📊 Chart cache initialized (max: {max_entries}, TTL: {ttl_seconds}s)")
    return _chart_cache


def get_cache() -> ChartCache:
    """Get the global chart cache instance"""
    global _chart_cache
    if _chart_cache is None:
        _chart_cache = ChartCache()
    return _chart_cache


def cache_chart(coin_id: str, chart_data: io.BytesIO) -> None:
    """Store a chart in cache"""
    cache = get_cache()
    cache.set(coin_id, chart_data)


def get_cached_chart(coin_id: str) -> Optional[io.BytesIO]:
    """Retrieve a chart from cache"""
    cache = get_cache()
    return cache.get(coin_id)


def cache_key(coin_id: str, vs_currency: str = "usd") -> str:
    """Generate cache key for a coin"""
    return f"{coin_id}_{vs_currency}"


class RateLimiter:
    """
    Simple rate limiter for API calls
    Implements exponential backoff for retries
    """
    
    def __init__(self, calls_per_minute: int = 50):
        self.calls_per_minute = calls_per_minute
        self.call_times = []
    
    async def wait_if_needed(self) -> None:
        """
        Check rate limit and wait if necessary
        """
        now = time.time()
        
        # Remove calls older than 1 minute
        self.call_times = [t for t in self.call_times if now - t < 60]
        
        if len(self.call_times) >= self.calls_per_minute:
            # Wait until oldest call is > 60 seconds old
            wait_time = 60.1 - (now - self.call_times[0])
            if wait_time > 0:
                logger.warning(f"⏳ Rate limit reached, waiting {wait_time:.1f}s")
                await asyncio.sleep(wait_time)
        
        self.call_times.append(time.time())
    
    def get_stats(self) -> Dict[str, any]:
        """Get rate limiter statistics"""
        now = time.time()
        recent_calls = len([t for t in self.call_times if now - t < 60])
        
        return {
            "calls_in_last_minute": recent_calls,
            "limit_per_minute": self.calls_per_minute,
            "utilization": f"{(recent_calls / self.calls_per_minute * 100):.1f}%"
        }


# Global rate limiter
_rate_limiter: Optional[RateLimiter] = None


def get_rate_limiter() -> RateLimiter:
    """Get the global rate limiter instance"""
    global _rate_limiter
    if _rate_limiter is None:
        _rate_limiter = RateLimiter(calls_per_minute=45)  # Conservative limit
    return _rate_limiter