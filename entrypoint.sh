#!/bin/sh

# Wait for the database to be ready
/usr/bin/wait-for-it.sh db:5432

# Load environment variables from .env file
if [ -f ".env" ]; then
  export $(cat .env | xargs)
fi

# Redundent
python /app/manage.py makemigrations

python /app/manage.py migrate --no-input
python /app/manage.py pollinate admin blogs

# Start the Django development server
python /app/manage.py runserver 0.0.0.0:8000
