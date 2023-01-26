from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import exc

from iot import models


from bot import models, schemas

async def get_latest_measurements(db: AsyncSession) -> list[models.Measurement]:
    user = await db.execute(select(models.User).where(models.User.telegram_id == platform_id))
    user: models.User = user.scalar()
    user.subscribed = subscription

    try:
        db.add(user)
        await db.commit()
        await db.refresh(user)
    except exc.IntegrityError:
        print()
    return subscription