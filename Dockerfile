# Use the official Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Set environment variable for Flask (optional)
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
