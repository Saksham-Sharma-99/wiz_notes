### WIZ_NOTES

#### ENV VARIABLES

```bash
DJANGO_SECRET_KEY=<super_secret_key>
DJANGO_ENVIRONMENT=<environment>
# database config
DATABASE_USER=<user>
DATABASE_PASSWORD=<password>
DATABASE_HOST=<host>
DATABASE_PORT=<port>
DATABASE_NAME=<database_name>
# s3 config
AWS_REGION=
AWS_BUCKET=
AWS_ACCESS_KEY=
AWS_SECRET_ACCESS_KEY=
# Celery Configuration Options
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

```

to start locally use sample.env file

```bash
cp sample.env .env
```

install requirements

```bash
pip install -r requirements.txt
```

to start server run

```bash
python manage.py runserver
```

to start celery process

```bash
celery -A wiz_notes worker --loglevel=info
```
