from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(ViewSet.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    