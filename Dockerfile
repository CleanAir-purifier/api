FROM python:3.7
#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
