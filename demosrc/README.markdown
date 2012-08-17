# A Demo

Example app, using `django-orderable`.

## Quick Start:

```shell
cd ~/Code
virtualenv --no-site-packages django-orderable

cd django-orderable
echo "export PIP_RESPECT_VIRTUALENV=true" >> bin/activate
echo "export PYTHONPATH=\"\$VIRTUAL_ENV/repo/src:\$VIRTUAL_ENV/repo/demosrc\"" >> bin/activate
echo "export DJANGO_SETTINGS_MODULE=\"orderabledemo.settings\"" >> bin/activate
source bin/activate

git clone git://github.com/mtigas/django-orderable.git repo

pip install -r $VIRTUAL_ENV/repo/demosrc/requirements.txt
```

You will probably need to `source bin/activate` or close your shell and
re-open it (so PATH picks up the correct `django-admin.py`).

Then:

```shell
django-admin.py syncdb --noinput
django-admin.py runserver
```

Note that the demo uses a SQLite database at `/tmp/orderabledemo.db`.

Visit http://127.0.0.1:8000/books/ and log in with the following test account:

* **Username:** demo
* **Password:** demo


