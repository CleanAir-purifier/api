FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./api-clean-air /api-clean-air
