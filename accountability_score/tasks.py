from celery import shared_task
from .models import AccountabilityScore, UserMetrics, DailyScoreLog
from .utils import calculate_score
import logging

logger = logging.getLogger(__name__)

@shared_task
def get_scores():
    try:
        user_metrics = UserMetrics.objects.all()
        for user_metric in user_metrics:
            try:
                current_score = AccountabilityScore.objects.get(user=user_metric.user).score
            except:
                current_score = None
            new_score = calculate_score(user_metric.task_count, user_metric.consistency,
                                        user_metric.account_age, user_metric.screen_time,
                                        user_metric.task_retention)
            AccountabilityScore.objects.filter(user=user_metric.user).update(score=new_score)
            AccountabilityScore.objects.filter(user=user_metric.user).update(prev_score=current_score)
            score_log = DailyScoreLog(user=user_metric.user, score=new_score)
            score_log.save()
            logger.info(f"Updated score {new_score} for {user_metric.user}")
            
    except Exception as e:
        logger.error(str(e))
