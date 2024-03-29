# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

# Install wkhtmltopdf
RUN apt update && apt install -y  \
    gettext  \
    nodejs  \
    npm  \
    wkhtmltopdf

RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py tailwind install