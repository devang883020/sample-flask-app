FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Non-root user for security (looks good on resume!)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run with gunicorn — 2 workers, production ready
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
