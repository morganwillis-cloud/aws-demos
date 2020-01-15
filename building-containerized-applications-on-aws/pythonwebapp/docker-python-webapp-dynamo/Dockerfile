# You can probably use a lighter image here
FROM ubuntu:16.04

MAINTAINER Morgan Willis "not-my-email@aws.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]