#!/usr/bin/env sh

if [ $(python3 /src/manage.py NecessaryDB) -eq 1 ];
then
    python3 /src/manage.py migrate
else
    python3 /src/manage.py migrate
fi

python3 /src/manage.py collectstatic --noinput

/usr/bin/uwsgi --ini /uwsgi/uwsgi.ini
