from fastapi import FastAPI, Response, status

from .controllers import mobile_sensors
from .controllers import purifiers

app = FastAPI()


@app.get("/purifier/{purifier_id}")
def get_purifier(purifier_id: int, response: Response):
    purifier = purifiers.get_purifier_by_id(purifier_id)
    if not purifier:
        response.status_code = status.HTTP_404_NOT_FOUND
    return purifier


@app.get("/mobile_sensor/{mobile_sensor_id}")
def get_mobile_sensor(mobile_sensor_id: int, response: Response):
    mobile_sensor = mobile_sensors.get_mobile_sensor_by_id(mobile_sensor_id)
    if not mobile_sensor:
        response.status_code = status.HTTP_404_NOT_FOUND
    return mobile_sensor


@app.patch("/mobile_sensor/{mobile_sensor_id}")
def patch_mobile_sensor_name(mobile_sensor_id: int, response: Response, name: mobile_sensors.UpdateMobileSensor):
    mobile_sensor = mobile_sensors.edit_mobile_sensor_name(mobile_sensor_id, name.dict())
    if not mobile_sensor:
        response.status_code = status.HTTP_404_NOT_FOUND
    return mobile_sensor
