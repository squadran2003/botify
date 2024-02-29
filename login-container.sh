#!/bin/bash

# Check if container name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <container_name>"
    exit 1
fi

# Container name
container_name=$1

# Run a Bash shell inside the container
docker exec -it $container_name sh
