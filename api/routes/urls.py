from django.urls import include, path
from . import views
from django.conf.urls import url

from .views import Directions, route_detail, create_route

urlpatterns = [
    url(r'^id/(?P<route_id>.*)', route_detail, name='route_detail'),
    url('create/', create_route, name='create_route'),
    path('directions/', Directions.as_view(), name='directions'),
]