#!/bin/sh

# Load environment variables from .env file
if [ -f ".env" ]; then
  export $(cat .env | xargs)
fi

# Wait for the database to be ready before starting the application
echo "Waiting for database to be ready..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done
echo "Database is ready!"

# Apply migrations
python /app/project/manage.py makemigrations
python /app/project/manage.py migrate

# Start the Django development server
python /app/project/manage.py runserver 0.0.0.0:8000
