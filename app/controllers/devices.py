from app.settings import db


def get_device_by_id(device_id: int):
    device_data = db.clean_air.find_one({"device.id": device_id})
    if device_data:
        return device_data['device']
