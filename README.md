# Goalwise Django App

## Setup

To install the dependencies and activate the virtual environment, run the following commands
in the project directory: 

```
poetry install
poetry shell
```

Now to start the project, just run:

```
python manage.py runserver
```

In a separate shell, start the redis server:

```
redis-server
```

Lastly, run the celery app:

```
celery -A goalwise worker --beat
```

You will also need to have a `.env` included in the goalwise service with the following secrets:

```
JWT_SECRET_KEY=your_secret_key
LOCAL_HOST=http://your_app_address
ALLOWED_HOSTS=http://your_allowed_host
ALLOWED_ORIGINS=http://your_allowed_origin
```

