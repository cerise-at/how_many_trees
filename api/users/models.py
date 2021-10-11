from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Overwrites the existing django User model.
    * 'Email' as primary key instead of 'username' and used for authentication.
    * 'Company' as new required field.
    """

    username = models.CharField(null=False, max_length=255)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    company_name = models.CharField(null=False, unique=True, max_length=255)
    emissions_CO2e = models.DecimalField(default=0.0, max_digits=19, decimal_places=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_dashboard(self):
            # TODO: sophisticated implementation of n_trees 
            #       and amount offset also given!
            # TODO: implement Route model!
            # "routes": [ route.get_overview() for route in Route.objects.get(fk=self.email) ]
            # TODO: implement Project model!
            # "projects": [ project.get_overview() for project in Project.objects.get(fk=self.email) ]
        dashboard = {
            "first_name": self.username,
            "company_name": self.company_name,
            "n_trees": f'{self.emissions_CO2e / 7 if self.emissions_CO2e > 0 else 0.0}',
            "routes": [
                {
                    "start_address": "address",
                    "stop_address": "address",
                    "emissions_CO2e": 100,
                    "distance_km": 100,
                    "vehicle_registration": "SA65 XXX"
                }
            ],
            "projects": [
                {
                    "project_title": "Project Title Placeholder",
                    "project_description": "Project Description Placeholder"
                }
            ]
        }
        return dashboard
