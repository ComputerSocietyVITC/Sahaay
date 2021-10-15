FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
LABEL IEEE ComSoc
ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt
COPY requirements/sql.txt postgres.txt
RUN pip install -r requirements.txt
RUN pip install -r postgres.txt

WORKDIR /Core
COPY /design /design
COPY /Core /Core


EXPOSE 3000