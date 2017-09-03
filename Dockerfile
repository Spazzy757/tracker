# use base python image with python 3.4
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
# Set Maintainer (as a label, MAINTAINER has been deprecated)
LABEL maintainer "brendan@tangentsolutions.co.za"
# set working directory to /app/
WORKDIR /code
ADD requirements.txt /code/
# install python dependencies
RUN pip install -U pip wheel setuptools
RUN pip install -r requirements.txt
ADD . /code/