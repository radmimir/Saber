# Saber Interactive test project 

Django, uWSGI and Nginx builded in a container using docker-compose

This project contains simple web-server, which parse the log-file using POST - requests. 

The application requires docker toolbox installed.

### Build and run
* go to the directory contains docker-compose.yml
* `docker-compose build`
* `docker-compose up -d` - daemon mode
* `docker-compose up`    - simple mode
* go to 127.0.0.1 to see if works

### Request format
* `POST /read_log 127.0.0.1:8001 {"offset" : 0}`
* `docker run -d -p 80:80 webapp`
* go to 127.0.0.1 to see if works

### How to insert your application

In /app currently a django project is created with startproject. You will
probably want to replace the content of /app with the root of your django
project. Then also remove the line of django-app startproject from the 
Dockerfile

uWSGI chdirs to /app so in uwsgi.ini you will need to make sure the python path
to the wsgi.py file is relative to that.
