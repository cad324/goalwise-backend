from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user-id/', CustomUserViewSet.as_view({'get': 'get_requested_user_id'}), name='get_requested_user_id')
]
