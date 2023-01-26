import datetime
import time

from fastapi import APIRouter, Depends, Request, Response

from sqlalchemy.ext.asyncio import AsyncSession

from bot import models, schemas, crud, bot
from iot.crud import get_latest_measurement

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
    if schema.message.text == "/subscribe" and not user.subscribed:
        ok = await crud.update_subscription(user.telegram_id, True, db)
        if not ok:
            print("subscribing failed")
            return
    if schema.message.text == "/unsubscribe" and user.subscribed:
        ok = await crud.update_subscription(user.telegram_id, False, db)
        if not ok:
            print("unsubscribing failed")
            return
    if schema.message.text == "/coffee":
        b = bot.BaseBotInterface()
        m = await get_latest_measurement(db)
        print(m)
        if time.time() - m.timestamp > 600:
            await b.send_message(user.telegram_id, "I'm sorry, my data is outdated.")
            return
        if m.temperature < 22.56:
            await b.send_message(user.telegram_id, "It might be a perfect time for a cup of espresso.")
            return
        if 22.56 < m.temperature < 23.9:
            await b.send_message(user.telegram_id, "It might be a crowd, but worth to check.")
            return
        if m.temperature > 23.9:
            await b.send_message(user.telegram_id, "Place is crowded, better drink some water.")
            return


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
