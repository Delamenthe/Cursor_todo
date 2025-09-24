#!/bin/sh
set -e

HOST="$POSTGRES_HOST"
PORT="$POSTGRES_PORT"

echo "Waiting for Postgres at $HOST:$PORT..."

until nc -z "$HOST" "$PORT" >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up"

