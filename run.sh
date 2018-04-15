#!/usr/bin/env sh

cp ./src/app/production_settings.py ./src/app/local_settings.py

if [ "$(src/manage.py NecessaryDB)" = "True" ];
then
    echo "NecessaryDB == TRUE"
    python3 src/manage.py migrate
else
    echo "NecessaryDB == FALSE"
    python3 src/manage.py migrate
    python3 src/manage.py loaddata src/casting/fixtures/*.json
fi

python3 src/manage.py collectstatic --noinput

sudo systemctl restart apache2