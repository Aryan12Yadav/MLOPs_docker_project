# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the host
EXPOSE 5000

# Set environment variable correctly
ENV FLASK_APP=app.py

# Run the Flask app correctly
CMD ["flask", "run", "--host=0.0.0.0"]
