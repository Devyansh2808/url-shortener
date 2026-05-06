from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class URLModel(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    clicks = Column(Integer, default=0)