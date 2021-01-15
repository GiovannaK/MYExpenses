FROM python:3.8.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:$PORT core.wsgi

COPY . .