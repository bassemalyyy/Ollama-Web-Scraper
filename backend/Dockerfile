FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY backend/ .  

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt
RUN pip install chainlit uvicorn

# Expose Fly.io default port
EXPOSE 8080

# Run FastAPI + Chainlit mounted app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]