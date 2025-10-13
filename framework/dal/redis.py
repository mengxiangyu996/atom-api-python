import redis
import threading


class _Redis:

    def __init__(self, redis_url: str):
        self._client = redis.Redis.from_url(redis_url, decode_responses=True)
        self._lock = threading.Lock()

    def close(self):
        self._client.connection_pool.disconnect()

    @property
    def client(self):
        return self._client