FROM python:3.10-slim

WORKDIR /project

COPY ./requirements.in ./
RUN pip install pip-tools && pip-compile requirements.in
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
