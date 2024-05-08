#!/bin/bash
cd ..
gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 & \
 celery -A app.utils.convert_txt:celery_app worker --loglevel=INFO
