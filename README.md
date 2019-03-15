# Simple python client for ci-workshop-app demo

Setup
```sh
# install dependencies
./setup.sh

# make requests to flask app running on localhost:8080
python client.py

# dump logs from elasticsearch (assumine EFKG stack is up and running) (see https://github.com/davified/efkg-docker-compose-example)
python elasticsearch_log_dump.py
```