from rest_framework import serializers

from .models import AccountabilityScore, UserMetrics


class AccountabilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountabilityScore
        fields = "__all__"


class UserMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMetrics
        fields = "__all__"
