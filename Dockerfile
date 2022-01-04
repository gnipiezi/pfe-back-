# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /boaa

# Set the working directory to /boaa
WORKDIR /boaa

# Copy the current directory contents into the container at /boaa
ADD . /boaa/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose 8000 by default
EXPOSE 8000/tcp

# Use runserver by default
CMD ["python", "/boaa/boaa/manage.py", "runserver", "0.0.0.0:8000"]
