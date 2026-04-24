FROM python:3.11-slim

WORKDIR /app

# Install system deps (optional but often needed)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . /app

# Run script
CMD ["python", "main.py"]
