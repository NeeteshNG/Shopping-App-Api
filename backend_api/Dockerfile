FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Run migrations, seed data, and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_products && gunicorn backend_api.wsgi:application --bind 0.0.0.0:8000"]
