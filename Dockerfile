# Dockerfile
FROM quay.io/aptible/ubuntu:14.04

# Basic dependencies
RUN apt-install build-essential python-dev python-setuptools
RUN apt-install libxml2-dev libxslt1-dev python-dev

RUN easy_install pip

# Add requirements.txt ONLY, then run pip install, so that Docker cache won't
# bust when changes are made to other repo files
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Add repo contents to image
ADD . /app/

ENV PORT 3000
EXPOSE 3000

