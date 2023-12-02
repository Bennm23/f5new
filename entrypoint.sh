#!/bin/sh

# Wait for the database to be ready
/usr/bin/wait-for-it.sh db:5432

# Load environment variables from .env file
if [ -f ".env" ]; then
  export $(cat .env | xargs)
fi


# Apply migrations for each app
python manage.py makemigrations f5index
python manage.py makemigrations f5store
python manage.py makemigrations f5blogs
python manage.py makemigrations f5teams

# Redundent
python /app/manage.py makemigrations

python /app/manage.py migrate --no-input
python /app/manage.py create_superuser
python /app/manage.py populate_teams

# Start the Django development server
python /app/manage.py runserver 0.0.0.0:8000
