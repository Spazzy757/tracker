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
        if queryset.count() > 2:
            while counter < return_count:
                point_one = queryset[counter]
                point_two = queryset[counter + 1]
                # VALUES
                first_point_timestamp = point_one.created
                second_point_timestamp = point_two.created
                time_diff = first_point_timestamp - second_point_timestamp
                seconds = time_diff.seconds
                origin = (float(point_one.latitude), float(point_one.longitude))
                destination = (float(point_two.latitude), float(point_two.longitude))
                # START OF CALCULATIONS
                distance = haversine.distance(origin=origin, destination=destination)*1000
                bearing = haversine.calculate_initial_compass_bearing(origin=origin, destination=destination)
                speed = haversine.speed(distance, seconds)
                data = {
                    'origin': {
                        'longitude': float(point_one.longitude),
                        'latitude': float(point_one.latitude),
                    },
                    'destination': {
                        'longitude': float(point_two.longitude),
                        'latitude': float(point_two.latitude),
                    },
                    'distance': distance,
                    'bearing': bearing,
                    'speed': speed
                }
                new_queryset.append(data)
                counter = counter+1
        # TODO: Change this to a pagination class
        if queryset.count() > 40:
            new_queryset = new_queryset[:40]
        return Response(new_queryset, status=200)
