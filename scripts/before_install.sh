#!/bin/bash

# Stop and remove the Docker container
cd /home/ubuntu/app/botify/
docker-compose -f docker-compose-prod.yaml down