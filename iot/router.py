from fastapi import APIRouter, Depends

from iot.schemas import SecurityData

from bot.crud import get_all_subscribed
from bot.bot import BaseBotInterface

from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session

iot_router = APIRouter(prefix="/iot", tags=["iot"])


@iot_router.post("/security")
async def security(request: SecurityData, db: AsyncSession = Depends(get_async_session)):
    if request.value > 900:
        users = await get_all_subscribed(db)
        bot = BaseBotInterface()
        for user in users:
            await bot.send_message(user.telegram_id, "Alarm!")
