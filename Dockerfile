FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ARG user
ARG uid

USER $user

RUN pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip install python-dotenv
RUN pip install statistics
