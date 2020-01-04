#!/bin/bash
echo "Logging into docker"
docker login
echo "Building docker image"
docker build -t {{ cookiecutter.docker_user }}/{{ cookiecutter.docker_repo }}:{{ cookiecutter.docker_tag }} .
echo "Pushing image to docker hub"
docker push {{ cookiecutter.docker_user }}/{{ cookiecutter.docker_repo }}:{{ cookiecutter.docker_tag }}