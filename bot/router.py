from fastapi import APIRouter, Depends, Request, Response

from sqlalchemy.ext.asyncio import AsyncSession

from bot import models, schemas, crud, bot
from db import get_async_session

telegram_router = APIRouter(prefix="/telegram", tags=["bots"])


@telegram_router.post("/webhook{token}")
async def telegram_bot_endpoint( request: Request, token: str, db: AsyncSession = Depends(get_async_session)):
    req = await request.json()

    try:
        schema = schemas.TelegramRequestBody(**req)
        if not schema.message.text:
            return Response(status_code=200)
        print(schema.message.text, schema.message.chat.username)
        # user = await upsert_telegram_user(schema, token, db)

    except Exception as e:
        return Response(status_code=200)


async def upsert_telegram_user(schema: schemas.TelegramRequestBody, token: str, db: AsyncSession) -> models.User:
    telegram_member = await bot.BaseBotInterface(token).get_info(schema.message.chat.id, schema.message.from_field.id)
    customer = await crud.read(telegram_member.user.id, db)

    if customer:
        return customer

    user_data = schemas.User(
        id=schema.message.from_field.id,
        username=telegram_member.user.username,
        first_name=telegram_member.user.first_name,
        last_name=telegram_member.user.last_name)

    return await crud.create(user_data, db)
