FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app

WORKDIR /app


RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt
