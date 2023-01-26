import uuid
import datetime

from sqlalchemy import Column, String, Float, BigInteger
from sqlalchemy.dialects.postgresql import UUID

from db import Base

from bot import schemas


class Measurement(Base):
    __tablename__ = "sensordataproject"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    luminosity = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    timestamp = Column(BigInteger)
