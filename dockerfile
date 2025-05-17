# Use official Python image as base
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install netcat (nc) for wait_for_db.sh script
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Copy the wait scripts and others
COPY wait_for_db.sh seed.sh entrypoint.sh ./

# Make them executable
RUN chmod +x wait_for_db.sh seed.sh entrypoint.sh

# Command to wait for DB, then start Django server
CMD ["./entrypoint.sh"]