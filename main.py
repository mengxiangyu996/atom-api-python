from config.config import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from framework import dal
from common import exception
from pathlib import Path


def main() -> FastAPI:
    # 创建FastAPI实例
    app = FastAPI(
        title=config.ruoyi.name,
        version=config.ruoyi.version
    )

    async def startup_event():
        try:
            # 启动时初始化数据库
            db_url = f"mysql+pymysql://{config.mysql.username}:{config.mysql.password}@{config.mysql.host}:{config.mysql.port}/{config.mysql.database}"
            dal.init_dabatase(db_url)

            # 启动时初始化redis
            # 无密码："redis://:@{config.redis.host}:{config.redis.port}/{config.redis.database}
            rds_url = f"redis://:{config.redis.password}@{config.redis.host}:{config.redis.port}/{config.redis.database}"
            dal.init_redis(rds_url)
        except Exception as e:
            raise Exception(f"服务初始化失败：{str(e)}") from e

    async def shutdown_event():
        dal.close_database()
        dal.close_redis()

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

    # 设置文件资源目录
    # 如果前端使用的是 history 路由模式，需要使用 nginx 代理，注释 admin 挂载逻辑
    # 如果前后端不分离方式部署需要配置前端为 hash 路由模式，解除 admin 挂载逻辑
    # admin_dir = Path("web/admin")
    # admin_dir.mkdir(parents=True, exist_ok=True)
    # app.mount(path="/admin", app=StaticFiles(directory=admin_dir), name="admin")
    # 设置上传文件目录
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
