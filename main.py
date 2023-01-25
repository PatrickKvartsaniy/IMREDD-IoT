import asyncio

import uvicorn


from fastapi import FastAPI

from config import config

from bot import telegram_router, BaseBotInterface
from iot import iot_router

app = FastAPI()
app.include_router(telegram_router)
app.include_router(iot_router)


@app.on_event('startup')
async def startup_event():
    await BaseBotInterface(config.telegram_token).set_webhook()


@app.on_event('shutdown')
async def shutdown_event():
    await BaseBotInterface(config.telegram_token).delete_webhook()


async def main():
    cfg = uvicorn.Config(
        "main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level.lower())
    server = uvicorn.Server(cfg)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
