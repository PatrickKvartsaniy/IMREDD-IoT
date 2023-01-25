import asyncio

import uvicorn


from fastapi import FastAPI, Request, Response

from config import config

app = FastAPI()
app.include_router(router)


@app.on_event('startup')
async def startup_event():
    pass


@app.on_event('shutdown')
async def shutdown_event():
    pass


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
