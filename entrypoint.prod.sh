#!/bin/sh

if [ "$DATABASE" = "multitenant" ]
then
    echo "esperando por postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started produccion"
fi

exec "$@"