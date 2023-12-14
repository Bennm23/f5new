#!/bin/sh

# Wait for the database to be ready
/usr/bin/wait-for-it.sh db:5432

# Load environment variables from .env file
if [ -f ".env" ]; then
  export $(cat .env | xargs)
fi
pwd
ls
# Redundent
python project/manage.py makemigrations

python project/manage.py migrate --no-input
python project/manage.py pollinate admin blogs

# Start the Django development server
python project/manage.py runserver 0.0.0.0:8000
