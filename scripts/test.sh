#!/bin/bash

cd ..
docker compose down
docker compose pull
docker compose up -d --build
pytest tests
docker compose down