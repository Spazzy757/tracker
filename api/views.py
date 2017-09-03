from rest_framework import viewsets
from api.models import Point
# Create your views here.


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
