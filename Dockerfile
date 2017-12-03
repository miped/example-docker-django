# Use an official Python runtime as a parent image
FROM python:2.7-slim

# To get better output or something?
# TODO: investigate
ENV PYTHONUNBUFFERED 1

# This container exposes a webserver on port 8070
EXPOSE 8070

# Install os requirements
RUN echo "Install os shit here"

# Install python requirements
ADD requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Set the working directory to /app/src
WORKDIR /app/src

# Run app.py when the container launches
# TODO: replace with uwsgi
CMD ["echo", "PRODUCTION"]
