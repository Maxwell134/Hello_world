FROM ubuntu

# Install Python
RUN apt-get update && \
    apt-get install -y python3

# Copy Python script
COPY dock.py /app/dock.py

# Set working directory
WORKDIR /app

# Run Python script
CMD ["python3", "dock.py"]
