FROM amd64/python:3.11.1-bullseye

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install unixodbc -y \
    && apt-get install unixodbc-dev -y \
    && apt-get install freetds-dev -y \
    && apt-get install freetds-bin -y \
    && apt-get install tdsodbc -y \
    && apt-get install --reinstall build-essential -y \
    && apt-get install curl -y \
    && apt-get install vim -y

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ADD ./config /climb-configs/

RUN mkdir /climb-app

COPY ./scripts/docker-entrypoint-prod.sh /docker-entrypoint.sh

ADD ./climb-app /climb-app/

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
