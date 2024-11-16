# Dockerfile

# Start from a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required packages
RUN pip install requests beautifulsoup4

# Copy the Python script into the container
COPY HoeWarmIsHetInDelft.py /app/HoeWarmIsHetInDelft.py

# Run the script
CMD ["python", "HoeWarmIsHetInDelft.py"]