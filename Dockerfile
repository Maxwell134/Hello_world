FROM ubuntu

# Install Apache
RUN apt-get update && \
    apt-get install -y apache2

# Copy HTML file to web server directory
COPY index.html /var/www/html/

# Expose port 80 for web traffic
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2ctl", "-D", "FOREGROUND"]
