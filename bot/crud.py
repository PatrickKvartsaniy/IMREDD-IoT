from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from bot import models, schemas


async def create(request: schemas.User, db: AsyncSession) -> models.User:
    customer = models.User(request)
    db.add(customer)
    await db.commit()
    await db.refresh(customer)
    return customer


async def read(platform_id: str, db: AsyncSession) -> models.User:
    customer = await db.execute(select(models.User).where(models.User.platform_id == platform_id))
    return customer.scalar()
