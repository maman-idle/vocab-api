web: gunicorn vocab_api.wsgi --log-file=-

release: python manage.py collectstatic -c --noinput
release: python manage.py migrate