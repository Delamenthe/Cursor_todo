#!/bin/sh
set -e

HOST="${POSTGRES_HOST:-db}"
PORT="${POSTGRES_PORT:-5432}"
USER="${POSTGRES_USER:-postgres}"
DB="${POSTGRES_DB:-best_todo}"

echo "Waiting for Postgres at $HOST:$PORT (db=$DB user=$USER) ..."

until pg_isready -h "$HOST" -p "$PORT" -U "$USER" >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up"

