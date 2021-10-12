from rest_framework import serializers
from .models import User, Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'company', 'emissions_CO2e']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Company.objects.create(name=validated_data['company'], user=user)
        return user