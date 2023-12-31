FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y python3-pymysql


COPY . .



CMD uvicorn app.main:app --host 0.0.0.0 --port 8885