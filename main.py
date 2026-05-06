from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string
from models import *

app = FastAPI()
urls_db = {}

@app.post("/shorten")
def shorten_url(url: URL):
    while True:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if short_url not in urls_db:
            break
    url_item = URLItem(
        **url.model_dump(),
        short_url=short_url,
        created_at=datetime.datetime.now(),
        clicks=0
    )
    urls_db[short_url] = url_item
    return url_item

@app.get("/s/{short_url}")
def redirect_url(short_url: str):
    url_item = urls_db.get(short_url)
    if url_item:
        url_item.clicks += 1
        return RedirectResponse(url_item.original_url)
    raise HTTPException("URL not found", status_code=404)

@app.get("/urls")
def get_urls():
    return list(urls_db.values())

@app.get("/urls/{short_url}")
def get_url(short_url: str):
    url_item = urls_db.get(short_url)
    if url_item:
        return url_item
    raise HTTPException("URL not found", status_code=404)

@app.delete("/urls/{short_url}")
def delete_url(short_url: str):
    if short_url in urls_db:
        urls_db.pop(short_url)
        raise HTTPException("URL deleted")
    raise HTTPException("URL not found", status_code=404)

