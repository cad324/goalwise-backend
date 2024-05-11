import os

from celery import Celery, signals
from celery.schedules import crontab


@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    pass


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goalwise.settings")
app = Celery("goalwise")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.timezone = "America/New_York"
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "[get_accountability_scores]": {
        "task": "accountability_score.tasks.get_scores",
        "schedule": crontab(),
    },
}
