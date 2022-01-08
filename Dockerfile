FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ARG user
ARG uid

USER $user

RUN pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip install python-dotenv

WORKDIR /home/$user

ENV PATH="/home/$user/.local/bin:${PATH}"

COPY --chown=myuser:$user . .

CMD [ "python","./main.py" ]