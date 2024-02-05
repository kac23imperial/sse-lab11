# Use the official Python image as the base image
FROM python

# Copy the requirements file to the current directory
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the contents of the ./api directory to the current directory in the image
COPY ./api/. ./

# Expose port 5000 for Flask to listen on
EXPOSE 5000

# Set the FLASK_APP environment variable to app.py
ENV FLASK_APP app.py

# Start the Flask application when the container is run
CMD ["flask", "run", "--host=0.0.0.0"]

# # Use an official Python runtime as a parent image
# FROM python:3.8-slim

# # Set the working directory in the container
# WORKDIR /python-docker

# # Copy the current directory contents into the container 
# COPY . /python-docker

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# # listen to requests that come from anywhere, not just localhost
# CMD ["python", "app.py"]
