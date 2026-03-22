#!/usr/bin/env bash
# docker build -t rknn-toolkit2 .
docker run -it -v "${PWD}:/usr/src/birdnet" --name rknn-toolkit2 rknn-toolkit2 bash
