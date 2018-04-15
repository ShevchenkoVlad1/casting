#!/usr/bin/env sh

if [ "$(src/manage.py NecessaryDB)" = "True" ];
then
    echo "NecessaryDB == TRUE"
    python3 src/manage.py migrate
else
    echo "NecessaryDB == FALSE"
    python3 src/manage.py migrate
fi

python3 src/manage.py collectstatic --noinput

sudo systemctl restart apache2