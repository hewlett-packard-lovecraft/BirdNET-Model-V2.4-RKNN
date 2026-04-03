#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

if [[ "${TRACE-0}" == "1" ]]; then set -o xtrace; fi

IMAGE_NAME=airockchip/rknn-toolkit2

if ! docker image inspect "$IMAGE_NAME" >/dev/null; then
    pushd ./rknn-toolkit2/rknn-toolkit2/docker/docker_file/ubuntu_20_04_cp38/ || exit

    docker build -t $IMAGE_NAME -f Dockerfile_ubuntu_20_04_for_cp38 .

    popd || exit
fi

if [ "$(docker ps -aq -f name=rknn-toolkit2)" ]; then
    echo "Removing rknn-toolkit2 container..."
    docker rm -f rknn-toolkit2
fi

docker build -t rknn-toolkit2 .

docker run -it -v "${PWD}:/usr/src/birdnet" --name rknn-toolkit2 rknn-toolkit2 bash
