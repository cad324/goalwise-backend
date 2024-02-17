from django.db import models
from django.contrib.auth.models import User
from goalwise.models import TimeStampMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class AccountabilityScore(TimeStampMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=500, validators=[MinValueValidator(300), MaxValueValidator(850)])
    prev_score = models.IntegerField(default=500, validators=[MinValueValidator(300), MaxValueValidator(850)])

    def __str__(self):
        return f'{self.user.last_name.upper()}, {self.user.first_name}  | Score: {self.score}'
    
class DailyScoreLog(TimeStampMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(300), MaxValueValidator(850)])
    date = models.DateField(blank=False, auto_now=True)

    def __str__(self):
        return f'{self.user.last_name.upper()}, {self.user.first_name}  | {self.date} | {self.score}'
    

class UserMetrics(TimeStampMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_count = models.PositiveIntegerField(default=0)
    consistency = models.FloatField(default=0.5, validators=[MinValueValidator(0), MaxValueValidator(1)])
    account_age = models.PositiveIntegerField(default=0)
    screen_time = models.PositiveIntegerField(default=0)
    task_retention = models.FloatField(default=0.95, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f'{self.user.last_name.upper()}, {self.user.first_name}  - Metrics'

    class Meta:
        verbose_name = 'User Metrics'
        verbose_name_plural = 'User Metrics'
