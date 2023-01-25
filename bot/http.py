from httpx import AsyncClient


async def post_request(url: str, payload: dict, headers: dict = None, params: dict = None):
    async with AsyncClient() as client:
        req = await client.post(url, json=payload, params=params, headers=headers)
        return req


async def get_request(url: str, headers: dict = None, params: dict = None):
    async with AsyncClient() as client:
        req = await client.get(url, params=params, headers=headers)
        return req
