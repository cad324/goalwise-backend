from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountabilityScoreViewSet

router = DefaultRouter()
router.register(r'accountability_score', AccountabilityScoreViewSet, basename='accountability-score')

urlpatterns = [
    path('api/', include(router.urls)),
]
