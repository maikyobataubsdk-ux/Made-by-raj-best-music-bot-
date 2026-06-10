import redis.asyncio as redis
from config import REDIS_URL

class RedisCache:
    def __init__(self):
        self._redis = None

    async def connect(self):
        if not self._redis:
            self._redis = redis.from_url(REDIS_URL, decode_responses=True)

    async def set(self, key, value, ex=None):
        await self.connect()
        await self._redis.set(key, value, ex=ex)

    async def get(self, key):
        await self.connect()
        return await self._redis.get(key)

    async def delete(self, key):
        await self.connect()
        await self._redis.delete(key)

redis_cache = RedisCache()
