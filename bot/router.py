from fastapi import APIRouter, Depends, Request, Response

from sqlalchemy.ext.asyncio import AsyncSession

from bot import models, schemas, crud, bot
from db import get_async_session

telegram_router = APIRouter(prefix="/telegram", tags=["bots"])


@telegram_router.post("/webhook")
async def telegram_bot_endpoint(request: Request, db: AsyncSession = Depends(get_async_session)):
    req = await request.json()
    schema = schemas.TelegramRequestBody(**req)
    if not schema.message.text:
        return Response(status_code=200)
    print(schema.message.text, schema.message.chat.username)
    user = await upsert_telegram_user(schema, db)
    print("user was created or already exists " + user.username)
    if schema.message.text == "/subscribe" and not user.subscribed:
        if not crud.update_subscription(user.telegram_id, True, db):
            print("subscribing failed")
            return
    if schema.message.text == "/unsubscribe" and user.subscribed:
        if not crud.update_subscription(user.telegram_id, False, db):
            print("unsubscribing failed")
            return
    if schema.message.text == "/coffee":
        pass


async def upsert_telegram_user(schema: schemas.TelegramRequestBody, db: AsyncSession) -> models.User:
    telegram_member = await bot.BaseBotInterface().get_info(schema.message.chat.id, schema.message.from_field.id)
    user = await crud.read(telegram_member.user.id, db)

    if user:
        print("user exists")
        return user

    user_data = schemas.User(
        id=schema.message.from_field.id,
        username=telegram_member.user.username,
        first_name=telegram_member.user.first_name,
        last_name=telegram_member.user.last_name)

    return await crud.create(user_data, db)
