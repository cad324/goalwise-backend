from django.db import models
from django.contrib.auth.models import User
from goalwise.models import TimeStampMixin
from django.core.validators import MinValueValidator, MaxValueValidator

class AccountabilityScore(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=500, validators=[MinValueValidator(300), MaxValueValidator(850)])
    prev_score = models.IntegerField(default=500, validators=[MinValueValidator(300), MaxValueValidator(850)])

    def __str__(self):
        return f'{self.user.username} | Score: {self.score}'
    
class DailyScoreLog(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(300), MaxValueValidator(850)])
    date = models.DateField(blank=False, auto_now=True)

    def __str__(self):
        return f'{self.user.username} | {self.date} | {self.score}'
    

class UserMetrics(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_count = models.PositiveIntegerField(default=0)
    consistency = models.FloatField(default=0.5, validators=[MinValueValidator(0), MaxValueValidator(1)])
    account_age = models.PositiveIntegerField(default=0)
    screen_time = models.PositiveIntegerField(default=0)
    task_retention = models.FloatField(default=0.95, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f'{self.user.username} - Metrics'

    class Meta:
        verbose_name = 'User Metrics'
        verbose_name_plural = 'User Metrics'
