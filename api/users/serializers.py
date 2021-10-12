from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'company', 'emissions_CO2e']

    # def create(self, validated_data):
    #     print(validated_data);
    #     password = validated_data.pop('password')
    #     user = super().create(validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

