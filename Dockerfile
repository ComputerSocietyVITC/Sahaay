FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
LABEL IEEE ComSoc

ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 3000

WORKDIR /Core
COPY /Core /Core

CMD ["uvicorn", "Core.asgi:fastapi", "--reload", "--port", "3000"]
# RUN adduser -D user
# USER user
