# Pin to a specific patch release of a minimal base image. In CI, pin by digest
# (FROM python:3.9.18-slim@sha256:...) and scan/sign the image before deployment.
FROM python:3.9.18-slim

ENV PYTHONUNBUFFERED=1

# Install PostgreSQL client (no recommended extras -> smaller attack surface)
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user/group to run the application (least privilege)
RUN groupadd --system appgroup \
    && useradd --system --gid appgroup --home-dir /app --shell /usr/sbin/nologin appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p static/uploads templates

COPY . .

# Least-privilege permissions (no world-writable 777) and non-root ownership
RUN chown -R appuser:appgroup /app \
    && chmod 755 static/uploads \
    && chmod +x /app/start.sh

# Drop root: run the container process as the unprivileged app user
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD python -c "import sys, urllib.request; sys.exit(0) if urllib.request.urlopen('http://127.0.0.1:5000/healthz', timeout=5).getcode() == 200 else sys.exit(1)"

CMD ["./start.sh"]
