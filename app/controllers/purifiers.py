from app.settings import db


def get_purifier_by_id(purifier_id: int):
    purifier_data = db.clean_air.find_one(
        {"device.id": purifier_id, "device.type": "purifier"})
    if purifier_data:
        return purifier_data['device']
