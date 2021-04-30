import os

from typing import Optional
from fastapi import FastAPI, Response, status

from app.settings import mongodb_settings
from app.controllers import devices as devices_controller

app = FastAPI()


@app.get("/device/{device_id}")
def get_device(device_id: int, response: Response):
    device = devices_controller.get_device_by_id(device_id)
    if not device:
        response.status_code = status.HTTP_404_NOT_FOUND
    return device


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
