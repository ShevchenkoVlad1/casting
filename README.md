# Movie Auditions & Casting

Create venv:

```sh
$ python3 -m venv ./venv
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cp .src/app/local_settings.py.example .src/app/local_settings.py
```

Django:
```sh
$ ./src/manage.py runserver
$ ./src/manage.py migrate
$ ./src/manage.py loaddata ./src/casting/fixtures/*.json
```

Translation:
```sh
$ ./src/manage.py makemessages --locale=en --extension html --extension py
$ ./src/manage.py makemessages --locale=ua --extension html --extension py
$ ./src/manage.py compilemessages
```
