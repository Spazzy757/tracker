from rest_framework import serializers
from api.models import Point


# first we define the serializers
class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Point
