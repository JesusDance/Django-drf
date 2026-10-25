FROM ghcr.io/astral-sh/uv:0.11.32 AS uv
FROM python:3.11-slim
WORKDIR /django_start
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_DEV=1
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --locked --no-install-project
COPY . .
CMD ["sh", "-c", "uv run python manage.py migrate && uv run python manage.py collectstatic --noinput && gunicorn django_start.wsgi:application --bind 0.0.0.0:8000"]