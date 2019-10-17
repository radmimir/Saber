FROM python:2.7

MAINTAINER Radmir Zaynullin <radm-z@yandex.ru>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	nginx
RUN pip install --upgrade pip
RUN pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY saber.conf /etc/nginx/sites-available/default
COPY uwsgi_params /etc/nginx/uwsgi_params

COPY requirements.txt /home/docker/code/app/
RUN pip install -r /home/docker/code/app/requirements.txt

COPY . /home/docker/code/

WORKDIR "/home/docker/code/"


