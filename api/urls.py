from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'^point', views.PointViewSet, base_name='point')
router.register(r'^movement', views.MovementViewSet, base_name='movement')
urlpatterns = [
    url(r'^', include(router.urls)),
]
