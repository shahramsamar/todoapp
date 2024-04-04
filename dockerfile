FROM python:3.11-slim-buster

LABEL maintainer="Shahramsamar2010@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /uer/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .

CMD [ "python","main.py" ]