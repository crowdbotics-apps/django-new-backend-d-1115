from rest_framework import viewsets
from homex.models import XXX
from .serializers import XXXSerializer


class XXXViewSet(viewsets.ModelViewSet):
    serializer_class = XXXSerializer
    queryset = XXX.objects.all()
