#!/usr/bin/env sh

if [ $(python3 src/manage.py NecessaryDB) -eq 1 ];
then
    python3 src/manage.py migrate
else
    python3 src/manage.py migrate
    python3 src/manage.py loaddata src/casting/fixtures/*.json
fi

sudo python3 src/manage.py collectstatic --noinput

uwsgi --ini uwsgi/production.ini