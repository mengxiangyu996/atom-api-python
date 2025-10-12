from config.config import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from framework.database import database
from framework.redis import redis
from common import exception
from pathlib import Path


def main() -> FastAPI:
    # 创建FastAPI实例
    app = FastAPI(
        title=config.ruoyi.name,
        version=config.ruoyi.version
    )

    # 在应用中注册数据访问层的生命周期管理器
    async def startup_event():
        try:
            # 启动时初始化数据库
            await database.init(
                db_url=f"mysql://{config.mysql.username}:{config.mysql.password}@{config.mysql.host}:{config.mysql.port}/{config.mysql.database}",
                modules={
                    "models": ["app.model"],
                },
                use_tz=False,
                timezone="Asia/Shanghai",
            )

            # 启动时初始化redis
            # 无密码："redis://:@{config.redis.host}:{config.redis.port}/{config.redis.database}
            await redis.init(
                redis_url=f"redis://:{config.redis.password}@{config.redis.host}:{config.redis.port}/{config.redis.database}"
            )
        except Exception as e:
            raise Exception(f"服务初始化失败：{str(e)}") from e

    async def shutdown_event():
        await database.close()
        await redis.close()

    # 注册启动和关闭事件
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)

    # 注册全局跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 注册异常处理
    exception.register_exception(app)

    # 挂载静态文件
    storage_dir = Path(config.ruoyi.upload_path)
    storage_dir.mkdir(parents=True, exist_ok=True)
    app.mount(path="/storage",
              app=StaticFiles(directory=storage_dir), name="storage")

    return app


if __name__ == "__main__":
    import uvicorn

    # 启动uvicorn服务器
    uvicorn.run(
        app="main:main",
        host=config.server.host,
        port=config.server.port,
        reload=config.server.debug,
        factory=True
    )
