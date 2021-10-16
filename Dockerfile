FROM python:3.9-buster
LABEL IEEE ComSoc
ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt

RUN pip install -r requirements.txt


WORKDIR /Core
COPY /design /design
COPY /Core /Core


EXPOSE 3000