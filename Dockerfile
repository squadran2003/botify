FROM python:3.10.13-bullseye


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/botify

COPY pyproject.toml poetry.lock ./



RUN pip install poetry


RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi



WORKDIR /usr/src/botify/botify
