# Saber Interactive test project 

Django, uWSGI and Nginx builded in a container using docker-compose

This project contains simple web-server, which parse the log-file using POST - requests. 

# The application requires:
 docker toolbox or docker desktop for windows: https://docs.docker.com/toolbox/toolbox_install_windows/
 docker for Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/

### Build and run
* go to the directory contains docker-compose.yml
* `docker-compose build`
* `docker-compose up -d` - daemon mode
* `docker-compose up`    - simple mode

### Stopping container
* `docker-compose down`

### Request format
* `POST / 127.0.0.1:8001 {"offset" : 0}`
