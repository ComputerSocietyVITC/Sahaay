FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
LABEL IEEE ComSoc

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 3000

WORKDIR /app
COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
# RUN adduser -D user
# USER user