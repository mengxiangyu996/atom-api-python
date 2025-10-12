import asyncio
import atexit
from types import ModuleType
from typing import Any
from tortoise import Tortoise, connections
from threading import Lock


class Database:
    """
    数据库连接管理器
    """

    _instance = None
    _instance_lock = Lock()

    def __new__(cls) -> "Database":
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
        atexit.register(self._cleanup)

    async def init(
        self,
        *,
        db_url: str,
        modules: dict[str, list[str | ModuleType]],
        **kwargs: Any,
    ) -> None:
        """
        初始化数据库连接。支持多模块配置，线程安全。
        Args:
            db_url: 数据库连接字符串
            modules: 模型模块字典
            **kwargs: 其他 Tortoise ORM 配置
        """

        async with self._init_lock:
            if not self._initialized:
                await Tortoise.init(db_url=db_url, modules=modules, **kwargs)
                self._initialized = True

    async def close(self) -> None:
        """
        关闭所有数据库连接
        """

        if not self._initialized:
            return

        await connections.close_all()
        self._initialized = False

    def _cleanup(self) -> None:
        """
        进程退出时自动调用，用于资源清理
        """

        if not self._initialized:
            return

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.close())
        except Exception as e:
            print(f"[Database Cleanup Error]: {e}")
        finally:
            loop.close()

    async def __aenter__(self) -> "Database":
        return self

    async def __aexit__(self, *exc_info) -> None:
        await self.close()


# 创建单例实例
database = Database()
