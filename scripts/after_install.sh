#!/bin/bash

# Change directory to your desired git repository
cd /home/ubuntu/app/botify/

# Perform git pull
git pull

docker-compose -f docker-compose-prod.yaml up --buld -d