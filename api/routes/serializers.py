from rest_framework import serializers
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            'email', 'start_address', 'end_address', 'distance_km', 
            'vehicle_registration', 'vehicle_emissions_CO2_km', 'coords'
            ]