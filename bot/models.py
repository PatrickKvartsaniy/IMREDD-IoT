import uuid
import datetime

from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

from db import Base

from bot import schemas


class User(Base):
    __tablename__ = "users"

    def __init__(self, schema: schemas.User):
        self.username = schema.username
        self.telegram_id = schema.id
        self.first_name = schema.first_name
        self.last_name = schema.last_name

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    subscribed = Column(Boolean, default=False)

    def get_id(self) -> str:
        return str(self.id)
