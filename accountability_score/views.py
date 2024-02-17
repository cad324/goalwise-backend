import logging
from accountability_score.models import AccountabilityScore, UserMetrics
from accountability_score.serializer import AccountabilityScoreSerializer, UserMetricsSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import F

logger = logging.getLogger(__name__)

class AccountabilityScoreViewSet(viewsets.ModelViewSet):

    queryset = AccountabilityScore.objects.all()
    serializer_class = AccountabilityScoreSerializer

    def retrieve(self, request, pk=None):
        score = AccountabilityScore.objects.filter(user=request.user.id)
        serializer = AccountabilityScoreSerializer(score)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserMetricsViewSet(viewsets.ModelViewSet):
    queryset = UserMetrics.objects.all()
    serializer_class = UserMetricsSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            field_name = request.data.get('field_name')
            increment_value = request.data.get('field_value', 0)

            if self.is_valid_field(field_name, UserMetrics):
                setattr(instance, field_name, F(field_name) + increment_value)
                instance.save()

                # Refresh instance to reflect new value from database
                instance.refresh_from_db()

                logger.info(f"Updated {field_name} for user {instance.user.id}. New value: {getattr(instance, field_name)}")

                # Return the updated instance
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                logger.error(f"Invalid field name '{field_name}' in update request.")
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid field name"})

        except UserMetrics.DoesNotExist:
            logger.error(f"UserMetrics object not found for user {request.user.id}.")
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "UserMetrics not found"})
        except Exception as e:
            logger.error(f"Unexpected error occurred while updating UserMetrics for user {request.user.id}.")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": str(e)})