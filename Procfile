release: python3 manage.py collectstatic --noinput
release: python3 manage.py rename_app crmapp main
release: python3 manage.py migrate --noinput
web: gunicorn crmproject.wsgi --log-file -
