#!/bin/sh

if [ "$DATABASE" = "multitenant" ]
then
    echo "esperando por postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started produccion"
fi

python manage.py migrate        # Apply database migrations
python manage.py collectstatic --clear --noinput # clearstatic files
python manage.py collectstatic --noinput  # collect static files

exec "$@"