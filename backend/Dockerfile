FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache curl \
    postgresql-dev \
    openssl-dev \
    musl-dev \
    libffi-dev \
    gcc \
    make \
    && pip install --no-cache-dir cryptography==2.1.4 \
    && pip3 install poetry==1.0.10
RUN mkdir /app
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-interaction --no-ansi --no-dev
COPY . /app/
RUN chmod +x entrypoint.sh
