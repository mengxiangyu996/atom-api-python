from config.config import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path


def main() -> FastAPI:
    # 创建FastAPI实例
    app = FastAPI(
        title=config.ruoyi.name,
    )

    # 注册全局跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 挂载静态文件
    storage_dir = Path(config.ruoyi.upload_path)
    storage_dir.mkdir(parents=True, exist_ok=True)
    app.mount(path="/storage", app=StaticFiles(directory=storage_dir), name="storage")

    return app


if __name__ == "__main__":
    import uvicorn

    # 启动uvicorn服务器
    uvicorn.run(
        app="main:main",
        host=config.server.host,
        port=config.server.port,
        reload=config.server.debug,
    )
