# This file is used by Docker Compose to build the images for the containers. 
# It installs required dependencies, copies the code, and 
# exposes the 8000 port.

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Install git
RUN apt-get update && apt-get upgrade -y && apt-get install -y git

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set working directory
WORKDIR /code

# copy dependencies
COPY requirements.txt /code/

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /code/

# expose port
EXPOSE 8000