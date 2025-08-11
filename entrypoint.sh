#!/bin/sh

# Esperar o PostgreSQL estar disponível
echo "Esperando o PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL iniciado."

# Aplicar migrações do Django
python manage.py migrate --no-input

# Coletar arquivos estáticos
python manage.py collectstatic --no-input

# Iniciar o Gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000