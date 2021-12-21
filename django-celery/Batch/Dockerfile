FROM python:3.8

RUN apt-get update
RUN mkdir /srv/code
ADD . /srv/code

WORKDIR /srv/code
ADD requirements.txt /srv/code
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt