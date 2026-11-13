FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/langeek

ENV PYTHONPATH=/app
ENV PORT=8080

EXPOSE 8080

CMD ["python3", "-m", "langeek.server"]
