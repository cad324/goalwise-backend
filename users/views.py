from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'

    def get_requested_user_id(self, request):
        id = request.user.id
        if id is not None:
            return Response({'id': id}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User ID not available'}, status=status.HTTP_401_UNAUTHORIZED)
