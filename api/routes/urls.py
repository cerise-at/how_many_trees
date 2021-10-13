from django.urls import include, path
from . import views

from .views import Directions

urlpatterns = [
    path('directions', Directions.as_view()),
]