# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV SOCIAL="facebook"
ENV CONFIG="/samples/like_top_5-share_2-posts.xml"
CMD python3 -m socialfeeder --social ${SOCIAL} --config ${CONFIG}