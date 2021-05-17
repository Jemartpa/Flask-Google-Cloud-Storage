#!/bin/bash

docker build -t "webdev1:Dockerfile" .
docker run -i -t "webdev1:Dockerfile"