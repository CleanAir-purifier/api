import os

from typing import Optional
from fastapi import FastAPI
import pymongo

from app.config import mongodb_settings

app = FastAPI()

client = pymongo.MongoClient(mongodb_settings)
db = client.clean_air


@app.get("/purifier_status")
def purifier_status():
    purifier_data = db.clean_air.find_one()
    return purifier_data['purifier']


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
