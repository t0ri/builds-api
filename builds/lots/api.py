from lots.models import Lot
from rest_framework import viewsets, permissions
from .serializers import LotSerializer

# Lot Viewset
class LotViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = LotSerializer
    
    def get_queryset(self):
        return self.request.user.lots.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)