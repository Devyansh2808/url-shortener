from pydantic import BaseModel
import datetime

class URL(BaseModel):
    original_url: str

class URLItem(URL):
    short_url: str
    created_at: datetime.datetime
    clicks: int = 0 

    class Config:
        from_attributes = True