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

python3 /src/manage.py collectstatic --noinput
python3 /src/manage.py compilemessages

sudo systemctl restart apache2