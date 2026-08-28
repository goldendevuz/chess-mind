FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir fastapi uvicorn python-chess pydantic sqlalchemy asyncpg alembic redis arq python-jose passlib
COPY app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

