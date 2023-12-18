from accountability_score.models import AccountabilityScore
from accountability_score.serializer import AccountabilityScoreSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class AccountabilityScoreViewSet(viewsets.ModelViewSet):

    queryset = AccountabilityScore.objects.all()
    serializer_class = AccountabilityScoreSerializer

    def retrieve(self, request, pk=None):
        score = AccountabilityScore.objects.filter(user=request.user.id)
        serializer = AccountabilityScoreSerializer(score)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        pass
    
    def destroy(self, request, *args, **kwargs):
        pass
    
    def update(self, request, *args, **kwargs):
        pass
    
    def partial_update(self, request, *args, **kwargs):
        pass
