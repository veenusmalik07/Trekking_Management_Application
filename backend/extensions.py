import os

from flask_mail import Mail
from flask_caching import Cache

mail = Mail()

cache = Cache(config={
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_URL": os.environ.get("CACHE_REDIS_URL", "redis://localhost:6379/1"),
    "CACHE_DEFAULT_TIMEOUT": 300
})
