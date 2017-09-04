from api.models import Point, Device
from django.contrib import admin
# Register your models here.


class PointAdmin(admin.ModelAdmin):
    list_display = ('device', 'longitude', 'latitude')

admin.site.register(Point, PointAdmin)
admin.site.register(Device)
