#!/bin/bash
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
