from django.contrib import admin

from .models import AccountabilityScore, DailyScoreLog, UserMetrics


@admin.register(AccountabilityScore)
class AccountabilityScoreAdmin(admin.ModelAdmin):
    list_display = ("user", "score")
    list_filter = ("user",)
    search_fields = ("user__username",)


@admin.register(DailyScoreLog)
class DailyScoreLogAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "score")
    list_filter = ("date", "user")
    search_fields = ("user__username",)
    date_hierarchy = "date"


@admin.register(UserMetrics)
class UserMetricsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "task_count",
        "consistency",
        "account_age",
        "screen_time",
        "task_retention",
    )
    list_filter = ("user",)
    search_fields = ("user__username",)
