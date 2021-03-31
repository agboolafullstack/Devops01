FROM python:3.6-alpine

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps

RUN pip install --upgrade pip
WORKDIR /time_stamps

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
