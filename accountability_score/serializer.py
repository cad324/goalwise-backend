from rest_framework import serializers
from .models import AccountabilityScore

class AccountabilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountabilityScore
        fields = '__all__'
