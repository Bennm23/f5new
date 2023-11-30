# Use the official Python image as a base image
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY ./project .

# Change permissions
RUN chmod -R 755 /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["python", "/app/project/manage.py", "runserver", "0.0.0.0:8000"]


