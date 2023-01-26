from fastapi import APIRouter, Depends, Request, Response

from iot.schemas import SecurityData

from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session

iot_router = APIRouter(prefix="/iot", tags=["iot"])


@iot_router.post("/stream")
async def data_stream(request: Request):
    req = await request.json()
    #
    # try:
    #     schema = schemas.TelegramRequestBody(**req)
    #     if not schema.message.text:
    #         return Response(status_code=200)
    #
    #     user = await upsert_telegram_user(schema, token, db)
    #
    # except Exception as e:
    #     return Response(status_code=200)
    print(req)


@iot_router.post("/security")
async def security(request: SecurityData):
    #
    # try:
    #     schema = schemas.TelegramRequestBody(**req)
    #     if not schema.message.text:
    #         return Response(status_code=200)
    #
    #     user = await upsert_telegram_user(schema, token, db)
    #
    # except Exception as e:
    #     return Response(status_code=200)
    print(req)

# async def upsert_telegram_user(schema: schemas.TelegramRequestBody, token: str, db: AsyncSession) -> models.User:
#     telegram_member = await bot.BaseBotInterface(token).get_info(schema.message.chat.id, schema.message.from_field.id)
#     customer = await crud.read(telegram_member.user.id, db)
#
#     if customer:
#         return customer
#
#     user_data = schemas.User(
#         id=schema.message.from_field.id,
#         username=telegram_member.user.username,
#         first_name=telegram_member.user.first_name,
#         last_name=telegram_member.user.last_name)
#
#     return await crud.create(user_data, db)
