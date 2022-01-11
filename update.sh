#!/bin/bash

git pull
docker build -t newhartian .
docker stop newhartian
docker rm newhartian
docker run -d --name newhartian --restart on-failure:5 --env-file .env newhartian