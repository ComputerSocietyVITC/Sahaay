FROM debian
LABEL IEEE ComSoc
ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt

RUN apt-get update -y && apt-get upgrade -y
RUN apt install python3.9 -y
RUN apt install pip -y
RUN pip install -r requirements.txt


WORKDIR /Core
COPY /design /design
COPY /Core /Core


EXPOSE 8080