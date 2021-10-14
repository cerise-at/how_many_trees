# from rest_framework import serializers
# from .models import User, Company


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'company', 'emissions_CO2e']

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Company.objects.create(name=validated_data['company'], user=user)
#         return user

from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer

from .models import Project



class CustomRegisterSerializer(RegisterSerializer):

    company = serializers.CharField(max_length=255)
    emissions_CO2e = serializers.DecimalField(default=0.0, max_digits=19, decimal_places=10)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        # data_dict['username'] = self.validated_data.get('username', '')
        data_dict['company'] = self.validated_data.get('company', '')
        data_dict['emissions_CO2e'] = self.validated_data.get('emissions_CO2e', '')
        return data_dict



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [ 'company', 'title', 'description',
                   'offset_emissions_CO2e', 'start_date', 'end_date' ]
