from pydantic import BaseModel
from typing import Optional

from app.settings import db


class UpdateMobileSensor(BaseModel):
    name: Optional[str] = None


def get_purifier(mobile_sensor_id):
    purifier_data = db.clean_air.find_one(    
        {"mobile_sensors.id": mobile_sensor_id}
    )
    return purifier_data


def get_mobile_sensor_by_id(mobile_sensor_id: int):
    purifier_data = get_purifier(mobile_sensor_id)
    if purifier_data:    
        mobile_sensor = [e for e in purifier_data["mobile_sensors"] if e["id"] == mobile_sensor_id]
        return mobile_sensor[0]


def edit_mobile_sensor_name(mobile_sensor_id: int, name: UpdateMobileSensor):
    purifier = get_purifier(mobile_sensor_id)

    updated = purifier["mobile_sensors"]
    for e in updated:
        if e["id"] == mobile_sensor_id:
            e["name"] = name["name"]

    purifier["mobile_sensors"] = updated

    mobile_sensor_data = db.clean_air.update_one(
        {"mobile_sensors.id":mobile_sensor_id}, {"$set": purifier}
    )
    if mobile_sensor_data:
        return get_mobile_sensor_by_id(mobile_sensor_id)
