FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
LABEL IEEE ComSoc

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /app
COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
# RUN adduser -D user
# USER user