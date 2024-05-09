#!/bin/bash
cd ..
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080 & \
 celery -A app.utils.convert_txt:celery_app worker --loglevel=INFO
