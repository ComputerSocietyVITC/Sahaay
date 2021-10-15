FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
LABEL IEEE ComSoc

ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt
RUN pip install -r requirements.txt



WORKDIR /Core
COPY /design /design
COPY /Core /Core


CMD ["uvicorn", "Core.asgi:fastapi", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]

EXPOSE 3000

# RUN adduser -D user
# USER user
