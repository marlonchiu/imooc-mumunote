import redis

from app.config.config import config
from app.settings import env

def redis_connect():
    redis_config = config[env]
    pool = redis.ConnectionPool(
        host=redis_config.REDIS_HOST,
        port=redis_config.REDIS_PORT,
        # password=redis_config.REDIS_PASSWORD,
        max_connections=redis_config.REDIS_POLL,
        db=redis_config.REDIS_DB,
        decode_responses=redis_config.REDIS_DECODE_RESPONSES,
    )
    return redis.Redis(connection_pool=pool)
