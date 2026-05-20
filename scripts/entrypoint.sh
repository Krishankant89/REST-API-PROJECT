#!/bin/sh

echo "Waiting for PostgreSQL..."

sleep 5

echo "Starting FastAPI application..."

cd ..

uvicorn app.main:app --host 0.0.0.0 --port 8000