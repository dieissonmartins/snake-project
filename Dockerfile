FROM python:3.8.3-alpine

RUN pip install --upgrade pip
RUN pip install mysql-connector-python


ARG user
ARG uid

#RUN adduser -D $user
USER $user

WORKDIR /home/$user

ENV PATH="/home/$user/.local/bin:${PATH}"

COPY --chown=myuser:$user . .

CMD [ "python","./main.py" ]