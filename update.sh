#!/bin/bash

git pull
docker rm newhartian
docker build -t newhartian .
docker container stop newhartian
docker rm newhartian
docker run -d --name newhartian --env-file .env newhartian