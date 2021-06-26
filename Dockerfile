# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

# install wget
RUN apt-get update
RUN apt install wget -y

# install chrome
RUN apt-get install software-properties-common -y
RUN apt-get install fonts-liberation libatk-bridge2.0-0 -y
RUN apt-get install libatk1.0-0 libatspi2.0-0 libasound2 -y
RUN apt-get install libcairo2 libcups2 libdrm2 libgbm1 -y
RUN apt-get install libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 -y
RUN apt-get install libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 -y
RUN apt-get install libxrandr2 libxshmfence1 xdg-utils -y
RUN apt-get update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb

# install socialfeeder
WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# entry point
ENV SOCIAL="facebook"
ENV CONFIG="/samples/like_top_5-share_2-posts.xml"
CMD python3 -m socialfeeder --social ${SOCIAL} --config ${CONFIG}