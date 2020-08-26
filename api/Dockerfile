# base image
FROM python:3.7.2-stretch

# Setup working directory
ENV CONTAINER_HOME=/usr/src/app
ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

# Expose the port uWSGI will listen on
EXPOSE 5000

# Add requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# Install requirements
RUN pip install -r requirements.txt