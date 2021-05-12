from pydantic import BaseModel
from typing import Optional

from app.settings import db


class UpdateMobileSensor(BaseModel):
    name: Optional[str] = None


def get_mobile_sensor_by_id(mobile_sensor_id: int):
    purifier_data = db.clean_air.find_one(    
        {"mobile_sensors.id": mobile_sensor_id}
    )
    if purifier_data:    
        mobile_sensor = [e for e in purifier_data["mobile_sensors"] if e["id"] == mobile_sensor_id]
        return mobile_sensor[0]
