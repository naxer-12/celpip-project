# Lightweight production Dockerfile for CELPIP Project
FROM python:3.11-slim

WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8001

# Install runtime dependencies
COPY celtestpip/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY celtestpip/ ./celtestpip/

# Expose server port
EXPOSE 8001

# Launch using uvicorn reading $PORT dynamically
CMD python3 celtestpip/server.py --port ${PORT:-8001}
