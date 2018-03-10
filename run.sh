#!/usr/bin/env sh

if [ "$(src/manage.py NecessaryDB)" = "True" ];
then
    echo "NecessaryDB == TRUE"
    python3 src/manage.py migrate
else
    echo "NecessaryDB == FALSE"
    python3 src/manage.py migrate
    python3 src/manage.py loaddata src/casting/fixtures/*.json
fi

sudo python3 src/manage.py collectstatic --noinput

uwsgi --ini uwsgi/production.ini