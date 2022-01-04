FROM python:3.8

ADD main.py .

RUN pip3 install --upgrade pip

# Arguments defined in docker-compose.yml
ARG user
ARG uid

RUN pip3 install --upgrade pip

RUN pip install requests beutifulsoup4

CMD [ "python","./main.py" ]