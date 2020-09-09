FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pkg-resources=3.3-1ubuntu1
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['main.py']