from api.models import Point, Device, Movement
from django.contrib import admin
# Register your models here.


class PointAdmin(admin.ModelAdmin):
    list_display = ('device', 'longitude', 'latitude')

admin.site.register(Device)
admin.site.register(Movement)
admin.site.register(Point, PointAdmin)
