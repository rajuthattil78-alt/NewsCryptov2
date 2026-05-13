"""
Database Management Module
Handles both JSON file storage and Redis caching
"""

import json
import os
import redis.asyncio as redis
from typing import Dict, List, Optional, Any
import logging
from datetime import datetime

import config

logger = logging.getLogger(__name__)

# ============================================================================
# GLOBAL REDIS CLIENT
# ============================================================================

_redis_client: Optional[redis.Redis] = None


async def get_redis() -> redis.Redis:
    """Get or initialize Redis connection (singleton pattern)"""
    global _redis_client
    if _redis_client is None:
        try:
            _redis_client = redis.from_url(
                config.REDIS_URL,
                decode_responses=True,
                socket_connect_timeout=10,
                socket_keepalive=True
            )
            # Test connection
            await _redis_client.ping()
            logger.info("✅ Redis connection established")
        except Exception as e:
            logger.error(f"❌ Redis connection failed: {e}")
            raise
    return _redis_client


async def close_redis():
    """Close Redis connection gracefully"""
    global _redis_client
    if _redis_client:
        await _redis_client.close()
        _redis_client = None
        logger.info("Redis connection closed")


# ============================================================================
# REDIS OPERATIONS (FOR REAL-TIME PRICES)
# ============================================================================

async def get_market_prices() -> List[Dict[str, Any]]:
    """
    Fetch real-time crypto prices from Redis
    Updated continuously by backend
    Returns: List of price dicts with symbol, price_usd, etc.
    """
    try:
        r = await get_redis()
        data = await r.get(config.REDIS_PRICE_KEY)
        if data:
            return json.loads(data)
        return []
    except Exception as e:
        logger.warning(f"⚠️ Redis fetch error: {e}")
        return []


# ============================================================================
# LOCAL JSON DATABASE (USER DATA & NEWS)
# ============================================================================

DB_FILE = os.path.join(os.path.dirname(__file__), config.DB_FILE_NAME)


def _load_data() -> Dict[str, Any]:
    """Load all data from JSON file"""
    if not os.path.exists(DB_FILE):
        return {
            "users": {},
            "news": {"seen_links": [], "queue": []}
        }
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading database: {e}")
        return {
            "users": {},
            "news": {"seen_links": [], "queue": []}
        }


def _save_data(data: Dict[str, Any]) -> bool:
    """Save all data to JSON file"""
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        logger.error(f"Error saving database: {e}")
        return False


# ============================================================================
# USER MANAGEMENT
# ============================================================================

def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user data by ID"""
    data = _load_data()
    return data["users"].get(str(user_id))


def user_exists(user_id: int) -> bool:
    """Check if user exists in database"""
    return get_user(user_id) is not None


def create_user(user_id: int) -> bool:
    """Create new user with default settings"""
    data = _load_data()
    data["users"][str(user_id)] = {
        "language": "en",
        "news_subscription": False,
        "created_at": datetime.now().isoformat()
    }
    return _save_data(data)


def update_user(user_id: int, key: str, value: Any) -> bool:
    """Update user field"""
    data = _load_data()
    if str(user_id) not in data["users"]:
        create_user(user_id)
        data = _load_data()
    
    data["users"][str(user_id)][key] = value
    return _save_data(data)


def get_all_users() -> Dict[str, Dict[str, Any]]:
    """Get all users (for broadcasts)"""
    return _load_data()["users"]


def get_subscribed_users() -> List[int]:
    """Get all user IDs with news subscription enabled"""
    users = get_all_users()
    return [
        int(uid) for uid, user_data in users.items()
        if user_data.get("news_subscription", False)
    ]


# ============================================================================
# NEWS MANAGEMENT
# ============================================================================

def add_news_item(item: Dict[str, Any]) -> bool:
    """Add news item to queue (avoid duplicates)"""
    data = _load_data()
    
    if item["link"] not in data["news"]["seen_links"]:
        data["news"]["seen_links"].append(item["link"])
        data["news"]["queue"].append({
            **item,
            "added_at": datetime.now().isoformat()
        })
        
        # Keep only last 100 items
        if len(data["news"]["queue"]) > 100:
            data["news"]["queue"] = data["news"]["queue"][-100:]
        
        return _save_data(data)
    
    return False


def get_news_queue() -> List[Dict[str, Any]]:
    """Get pending news queue"""
    return _load_data()["news"]["queue"]


def pop_news_batch(batch_size: int = 3) -> List[Dict[str, Any]]:
    """Remove and return first N news items"""
    data = _load_data()
    batch = data["news"]["queue"][:batch_size]
    data["news"]["queue"] = data["news"]["queue"][batch_size:]
    _save_data(data)
    return batch


def get_news_stats() -> Dict[str, int]:
    """Get news statistics"""
    data = _load_data()
    return {
        "seen_links": len(data["news"]["seen_links"]),
        "pending": len(data["news"]["queue"])
    }