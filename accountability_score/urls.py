from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountabilityScoreViewSet, UserMetricsViewSet

router = DefaultRouter()
router.register(r'accountability_score', AccountabilityScoreViewSet, basename='accountability-score')
router.register(r'usermetrics', UserMetricsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
