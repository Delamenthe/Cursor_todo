FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update && apt-get install -y build-essential libpq-dev netcat-traditional && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=best_todo.settings

COPY scripts/wait_for_db.sh /wait_for_db.sh
RUN chmod +x /wait_for_db.sh

CMD ["sh", "-c", "/wait_for_db.sh && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


