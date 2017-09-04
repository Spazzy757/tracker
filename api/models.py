from api.haversine import speed, distance, calculate_initial_compass_bearing
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


# Create your models here.
class Device(models.Model):
    custom_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.custom_id


class Point(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField(max_length=1000)
    latitude = models.FloatField(max_length=1000)
    device = models.CharField(max_length=1000)

    def __str__(self):
        return "long: {}, Lat: {}".format(str(self.longitude), str(self.latitude))

    class Meta:
        ordering = ('-created',)


class Movement(models.Model):
    movement_destination = models.ForeignKey(Point, related_name='destination')
    movement_origin = models.ForeignKey(Point, related_name='origin')
    speed = models.FloatField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField(max_length=1000)
    bearing = models.FloatField(max_length=1000)


@receiver(post_save, sender=Point)
def add_movement(created, instance, **kwargs):
    if created:
        custom_id = instance.device
        queryset = Point.objects.filter(device=custom_id)
        if queryset.count() > 1:
            origin = queryset[1]
            origin_coordinates = (origin.latitude, origin.longitude)
            destination_coordinates = (instance.latitude, instance.longitude)
            first_point_timestamp = origin.created
            second_point_timestamp = instance.created
            time_diff = second_point_timestamp - first_point_timestamp
            seconds = time_diff.seconds
            movement_distance = distance(origin_coordinates, destination_coordinates)*1000
            movement_bearing = calculate_initial_compass_bearing(origin_coordinates, destination_coordinates)
            movement_speed = speed(movement_distance, seconds)
            movement = Movement(
                speed=float(movement_speed),
                movement_origin=origin,
                bearing=movement_bearing,
                distance=movement_distance,
                movement_destination=instance,
            )
            movement.save()
