from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from iot import models


async def get_latest_measurement(db: AsyncSession) -> models.Measurement:
    m = await db.execute(select(models.Measurement).order_by(models.Measurement.timestamp.desc()))
    return m.scalar()
