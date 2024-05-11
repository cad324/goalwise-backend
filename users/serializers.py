from rest_framework import serializers

from accountability_score.models import AccountabilityScore, UserMetrics

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
            init_metrics = UserMetrics.objects.create(
                user=user,
                task_count=0,
                consistency=0.685,
                account_age=0,
                task_retention=1,
            )
            init_score = AccountabilityScore.objects.create(user=user, score=560)
            init_metrics.save()
            init_score.save()
        user.save()

        return user
