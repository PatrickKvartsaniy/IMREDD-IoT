from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import exc


from bot import models, schemas


async def create(request: schemas.User, db: AsyncSession) -> models.User:
    customer = models.User(request)
    db.add(customer)
    await db.commit()
    await db.refresh(customer)
    return customer


async def read(platform_id: str, db: AsyncSession) -> models.User:
    user = await db.execute(select(models.User).where(models.User.platform_id == platform_id))
    return user.scalar()


async def update_subscription(platform_id: str, subscription: bool, db: AsyncSession) -> bool:
    user = await db.execute(select(models.User).where(models.User.platform_id == platform_id))
    user: models.User = user.scalar()
    user.subscribed = subscription

    try:
        db.add(user)
        await db.commit()
        await db.refresh(user)
    except exc.IntegrityError:
        print()
    return subscription


async def get_all_subscribed(db: AsyncSession) -> list[models.User]:
    users = await db.execute(select(models.User).where(models.User.subscribed == True))
    return users.scalars().all()
