FROM python:3.11

WORKDIR /app

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml ./

RUN poetry install --no-root

COPY src .

EXPOSE 8000