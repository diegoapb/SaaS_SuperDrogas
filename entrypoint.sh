#!/bin/sh

if [ "$DATABASE" = "multitenant" ]
then
    echo "Esperando la coneccion con postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL iniciado"
fi

python manage.py flush --no-input
python manage.py migrate
# En pruebas
python manage.py collectstatic --no-input --clear

exec "$@"