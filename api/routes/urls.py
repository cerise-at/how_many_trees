from django.urls import include, path
from . import views
from django.conf.urls import url

from .views import Directions, route_detail

urlpatterns = [
    url(r'^id/(?P<route_id>.*)', route_detail, name='route_detail'),
    path('directions/', Directions.as_view(), name='directions'),
]