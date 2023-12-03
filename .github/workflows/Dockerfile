FROM ubuntu

# Install Python
RUN apt-get update && \
    apt-get install -y python3

WORKDIR /app
# Copy Python script
COPY dock.py /app

# Set working directory


# Run Python script
CMD ["python3", "dock.py"]
