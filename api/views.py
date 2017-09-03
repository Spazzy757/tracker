# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from api.serializers import PointSerializer
from rest_framework import viewsets
from api.models import Point
# Create your views here.


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    # authentication_class = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PointSerializer
