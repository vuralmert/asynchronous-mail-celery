# Django base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .

# Copy the project files to the working directory
COPY . .

# Expose the application port
EXPOSE 8000

# Run migrations and create superuser on container startup
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py initadmin
RUN python manage.py inituser

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]