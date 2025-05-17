#!/bin/sh

echo "Waiting for Postgres..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Postgres is up!"

echo "Waiting for Elasticsearch..."
while ! nc -z elasticsearch 9200; do
  sleep 1
done
echo "Elasticsearch is up!"
