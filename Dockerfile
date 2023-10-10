# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install python3-dev build-essential -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "uvicorn", "server:app", "--host", "0.0.0.0" ]