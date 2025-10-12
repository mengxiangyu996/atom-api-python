import asyncio
import atexit
from threading import Lock
from redis.asyncio import Redis as RedisClient, ConnectionPool


class Redis:
    """
    Redis连接管理器
    """

    _instance = None
    _instance_lock = Lock()

    def __new__(cls) -> "Redis":
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if hasattr(self, "_initialized_flag"):
            return

        self._initialized_flag = True
        self._initialized = False
        self._init_lock = asyncio.Lock()
        self._redis: RedisClient | None = None
        self._pool: ConnectionPool | None = None

        atexit.register(self._cleanup)

    async def init(
        self,
        *,
        redis_url: str,
        decode_responses: bool = True,
        **kwargs,
    ) -> None:
        """
        初始化Redis连接

        Args:
            redis_url: Redis连接字符串 (如 redis://localhost:6379/0)
            decode_responses: 是否自动解码响应
            **kwargs: 其他连接参数
        """

        async with self._init_lock:
            if not self._initialized:
                self._pool = ConnectionPool.from_url(
                    url=redis_url,
                    decode_responses=decode_responses,
                    **kwargs,
                )
                self._redis = RedisClient(connection_pool=self._pool)
                await self._redis.ping()
                self._initialized = True

    async def close(self) -> None:
        """
        关闭Redis连接
        """

        if not self._initialized:
            return

        if self._redis is not None:
            await self._redis.aclose()
        if self._pool is not None:
            await self._pool.disconnect()

        self._redis = None
        self._pool = None
        self._initialized = False

    def _cleanup(self) -> None:
        """
        程序退出时的清理逻辑
        """

        if not self._initialized:
            return

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.close())
        except Exception as e:
            print(f"[Redis Cleanup Error]: {e}")
        finally:
            loop.close()

    async def __aenter__(self) -> "Redis":
        return self

    async def __aexit__(self, *exc_info) -> None:
        await self.close()

    @property
    def client(self) -> RedisClient:
        """
        获取Redis客户端实例
        """

        if not self._initialized or self._redis is None:
            raise RuntimeError("Redis未初始化或客户端不可用")
        return self._redis

    async def ping(self) -> bool:
        """
        测试连接
        """

        try:
            return await self.client.ping()
        except Exception:
            return False


# 创建单例实例
redis = Redis()
