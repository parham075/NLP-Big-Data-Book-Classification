FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# INSTALL OS DEPENDENCIES
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y curl unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4

# INSTALL CHROME
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get -y update \
    && apt-get -y install google-chrome-stable

# INSTALL PYTHON DEPENDENCIES
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy Environment Variables - if you haven't created a ".env" file, please create one from "env.example"
COPY .env .env

# COPY & RUN TEST SCRIPT
COPY . .
CMD ["python3", "web_crawling.py"]