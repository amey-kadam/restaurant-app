# Use official Python image
FROM python:3.11-slim

# Prevents writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Expose port for the app & WebSockets
EXPOSE 8080

# Start your Flask-SocketIO app via Gunicorn + eventlet
CMD ["gunicorn", "--worker-class", "eventlet", "--bind", "0.0.0.0:8080", "app:create_app()"]
