from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Overwrites the existing django User model.
    * Remove 'username' field
    * Add 'first_name' and 'surname' required fields.
    * 'Email' as primary key instead of 'username' and used for authentication.
    * 'Company' as new required field.
    """

    username = None
    first_name = models.CharField(null=False, max_length=255)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    company_name = models.CharField(null=False, unique=True, max_length=255)
    emissions_CO2e = models.DecimalField(default=0.0, max_digits=19, decimal_places=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_dashboard(self):
        dashboard = {
            "first_name": self.username,
            "company_name": self.company_name,

            # TODO: sophisticated implementation of n_trees 
            #       and amount offset also given!
            "n_trees": f'{self.emissions_CO2e / 7}',

            # TODO: implement Route model!
            # "routes": [ route.get_overview() for route in Route.objects.get(fk=self.email) ]
            "routes": [
                {
                    "start_address": "address",
                    "stop_address": "address",
                    "emissions_CO2e": 100,
                    "distance_km": 100,
                    "vehicle_registration": "SA65 XXX"
                }
            ],
            # TODO: implement Project model!
            # "projects": [ project.get_overview() for project in Project.objects.get(fk=self.email) ]
            "projects": [
                {
                    "project_title": "Project Title Placeholder",
                    "project_description": "Project Description Placeholder"
                }
            ]
        }
        return dashboard
