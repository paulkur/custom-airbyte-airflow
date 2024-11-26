#!/bin/bash

# Bring down the production environment
sudo docker compose -f docker-compose.yml down --volumes --rmi all

# Bring down the development environment
sudo docker compose -f docker-compose-dev.yml down --volumes --rmi all

# Remove all docker volumes
sudo docker volume rm $(sudo docker volume ls -q)

# Remove all docker containers
sudo docker container prune -f

# Remove all unused networks
sudo docker network prune -f

# Remove all unused images
sudo docker image prune -f

# Remove all docker images, containers and volumes
sudo docker system prune -f

# Remove all docker volumes
sudo docker volume prune -f

# Remove all docker volumes with the system prune
sudo docker system prune --volumes -f

# Change to the airflow directory
cd airflow || { echo "Airflow directory not found"; exit 1; }

# Remove the logs directory if it exists
if [ -d "logs" ]; then
    sudo rm -rf logs
    echo "Old logs directory removed"
else
    echo "No existing logs directory found"
fi

# Create a new logs directory
sudo mkdir -p logs
echo "New logs directory created"

# Set permissions for the logs directory
sudo chmod -R 777 logs
echo "Permissions set for the logs directory"

# Print success message
echo "Logs directory cleaned and permissions set successfully"
