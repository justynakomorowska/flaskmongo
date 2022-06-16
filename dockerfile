FROM python:3.7-buster

ENV FLASK_CONFIG production
ENV FLASK_APP app.py
#RUN adduser -D flasky
#USER flasky

WORKDIR /home/flask_shop

COPY requirements requirements
RUN apt-get update
RUN apt-get install -y build-essential


RUN python -m venv venv
RUN pip install --upgrade pip
RUN venv/bin/pip install -r requirements/docker.txt

COPY app ./app
COPY boot.sh ./
COPY app.py ./app.py
COPY localhost.crt ./
COPY localhost.key ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]