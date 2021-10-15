from rest_framework import serializers
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            'email', 'start_address', 'end_address', 'distance_km', 'name', 'emissions',
            'vehicle_registration', 'vehicle_class', 'vehicle_emissions_CO2e_km', 'coords'
            ]
