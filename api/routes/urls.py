from django.urls import include, path
from . import views

from .views import RouteViews

urlpatterns = [
    path('', RouteViews.as_view()),
]