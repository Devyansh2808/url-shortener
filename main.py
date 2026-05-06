from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
import random
import string
from models import *
from database import Base, engine, SessionLocal
from database_models import URLModel
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def shorten_url(url: URL, db: Session = Depends(get_db)):
    while True:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if not db.query(URLModel).filter(URLModel.short_url == short_url).first():
            break
    
    db_url = URLModel(
        original_url=url.original_url,
        short_url=short_url
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

@app.get("/s/{short_url}")
def redirect_url(short_url: str, db: Session = Depends(get_db)):
    url_item = db.query(URLModel).filter(URLModel.short_url == short_url).first()
    if not url_item:
        raise HTTPException(status_code=404, detail="URL not found")
    url_item.clicks += 1
    db.commit()
    db.refresh(url_item)
    return RedirectResponse(url_item.original_url)


@app.get("/urls")
def get_urls(db: Session = Depends(get_db)):
    db = SessionLocal()
    urls = db.query(URLModel).all()
    return urls

@app.get("/urls/{short_url}")
def get_url(short_url: str, db: Session = Depends(get_db)):
    url_item = db.query(URLModel).filter(URLModel.short_url == short_url).first()
    if url_item:
        return url_item
    raise HTTPException(status_code=404, detail="URL not found")

@app.delete("/urls/{short_url}")
def delete_url(short_url: str, db: Session = Depends(get_db)):
    url_item = db.query(URLModel).filter(URLModel.short_url == short_url).first()
    if not url_item:
        raise HTTPException(status_code=404, detail="URL not found")
    db.delete(url_item)
    db.commit()
    raise HTTPException(status_code=200, detail="URL deleted")

