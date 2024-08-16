# FROM ubuntu

# # Install Apache
# RUN apt-get update && \
#     apt-get install -y apache2

# # Copy HTML file to web server directory
# COPY index.html /var/www/html/

# # Expose port 80 for web traffic
# EXPOSE 80

# # Start Apache in the foreground
# CMD ["apache2ctl", "-D", "FOREGROUND"]

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to the host
EXPOSE 80

# Command to run the application
CMD ["python3", "main.py"]
















