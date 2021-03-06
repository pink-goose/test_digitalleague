FROM python:3.11-rc-slim

COPY requirements.txt .

RUN apk add libffi-dev g++ --no-cache && \
    sudo apt install libpq-dev
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt --no-cache-dir

WORKDIR /code/

COPY ./src/ /code/