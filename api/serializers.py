from api.models import Point, Movement
from rest_framework import serializers


# first we define the serializers
class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('longitude', 'latitude', 'created')
        model = Point


class MovementSerializer(serializers.ModelSerializer):
    movement_destination = PointSerializer()
    movement_origin = PointSerializer()

    class Meta:
        fields = ('speed', 'distance', 'bearing', 'movement_destination', 'movement_origin')
        model = Movement
        depth = 1
