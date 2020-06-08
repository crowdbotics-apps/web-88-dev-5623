from rest_framework import authentication
from users.models import WGWEtgrgtrt
from .serializers import WGWEtgrgtrtSerializer
from rest_framework import viewsets


class WGWEtgrgtrtViewSet(viewsets.ModelViewSet):
    serializer_class = WGWEtgrgtrtSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = WGWEtgrgtrt.objects.all()
