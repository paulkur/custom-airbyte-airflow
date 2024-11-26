#!/bin/bash

# Start the init-db service
#docker compose up -d --build init-db
# Wait for the init-db service to finish initializing the database
#sleep 10

docker compose -f docker-compose.yml build --no-cache

# Start the other services
#docker compose up -d
docker compose -f docker-compose.yml up -d


# Wait for containers to start
sleep 10

# Check running containers
docker ps

#sleep 10

# Remove the init-db container
#docker compose rm -f -s init-db


