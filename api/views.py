# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import PointSerializer
from rest_framework import viewsets
from api.models import Point
from api import haversine
# Create your views here.


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    # authentication_class = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PointSerializer


class MovementViewSet(viewsets.GenericViewSet):
    queryset = Point.objects.all()

    @classmethod
    def list(cls, request):
        device = request.GET.get('device')
        queryset = Point.objects.filter(device=device).order_by('-pk')
        counter = 0
        return_count = queryset.count() - 1
        new_queryset = []
        print("HERE")
        while counter < return_count:
            point_one = queryset[counter]
            point_two = queryset[counter + 1]
            print(float(point_one.latitude), float(point_one.longitude))
            origin = (float(point_one.latitude), float(point_one.longitude))
            destination = (float(point_two.latitude), float(point_two.longitude))

            distance = haversine.distance(origin=origin, destination=destination)
            bearing = haversine.calculate_initial_compass_bearing(origin=origin, destination=destination)
            data = {
                'pointOne': {
                    'longitude': point_one.longitude,
                    'latitude': point_one.longitude,
                },
                'pointTwo': {
                    'longitude': point_two.longitude,
                    'latitude': point_two.longitude,
                },
                'distance': distance,
                'bearing': bearing
            }
            new_queryset.append(data)
            counter = counter+1
        return Response(new_queryset, status=200)
