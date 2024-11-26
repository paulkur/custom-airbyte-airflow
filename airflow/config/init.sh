#!/usr/bin/env bash

airflow users create \
    --username johndoe \
    --firstname John \
    --lastname Doe \
    --role Admin \
    --email johndoe@gmail.com \
    --password 'SuperSecretPassword123'

#airflow variables import ./files/include/config/keys.json
#airflow connections import ./files/include/config/connections.json

