from django.urls import include, path
from . import views
from django.conf.urls import url

from .views import Directions, route_detail, create_route, update_route

urlpatterns = [
    url('create/', create_route, name='create_route'),
    url('update/', update_route, name='update_route'),
    path('directions/', Directions.as_view(), name='directions'),
    url(r'^(?P<route_id>.*)', route_detail, name='route_detail'),
]
