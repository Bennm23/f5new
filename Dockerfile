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

# Copy the entrypoint script into the container at /app
COPY entrypoint.sh .

# Install wait-for-it
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /usr/bin/wait-for-it.sh
RUN chmod +x /usr/bin/wait-for-it.sh

# Change permissions
RUN chmod +x entrypoint.sh

# Expose port 8000 to the outside world
EXPOSE 8000

# Specify the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]


