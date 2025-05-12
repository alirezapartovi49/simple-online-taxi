FROM python:3.12.4-alpine as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src 

WORKDIR /app

FROM base as builder

RUN apk update

RUN pip install -U uv

COPY alembic.ini pyproject.toml requirements.lock ./

RUN uv pip install --no-cache --system -r requirements.lock

COPY src/simple_online_taxi/ src/

FROM base as production

ENV PYTHONPATH=/app/src
COPY --from=builder /app /app

RUN python -m alembic upgrade head

EXPOSE 8000
CMD ["uvicorn", "src.simple_online_taxi.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base as development

ENV PYTHONPATH=/app/src
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

EXPOSE 8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.simple_online_taxi.main:app --host 0.0.0.0 --port 8000 --reload"]