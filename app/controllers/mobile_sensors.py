from app.settings import db


def get_mobile_sensor_by_id(mobile_sensor_id: int):
    mobile_sensor_data = db.clean_air.find_one(
        {"device.id": mobile_sensor_id, "device.type": "mobile_sensor"})
    if mobile_sensor_data:
        return mobile_sensor_data['device']
