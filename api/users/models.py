from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from routes.models import Route

from .managers import CustomUserManager



class User(AbstractUser):
    """
    Overwrites the existing django User model.
    * 'Email' as primary key instead of 'username' and used for authentication.
    * 'Company' as new required field.
    """

    username = None
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    company = models.CharField(null=False, unique=True, max_length=255)
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
        routes = [ route.get_overview() for route in Route.objects.filter(email=self.email) ]
            # TODO: implement Project model!
            # "projects": [ project.get_overview() for project in Project.objects.get(fk=self.email) ]
        dashboard = {
            "first_name": self.username,
            "company_name": self.company,
            "n_trees": f'{self.emissions_CO2e / 7 if self.emissions_CO2e > 0 else 0.0}',
            "routes": routes,
            "projects": [
                {
                    "project_title": "Project Title Placeholder",
                    "project_description": "Project Description Placeholder"
                }
            ]
        }
        return dashboard



class Project(models.Model):

    company = models.CharField(null=False, unique=True, max_length=255)
    title = models.CharField(null=False, unique=True, max_length=255)
    description = models.CharField(null=False, unique=True, max_length=510)
    offset_emissions_CO2e = models.DecimalField(default=0.0, max_digits=19, decimal_places=10)
    start_date = DateField()
    end_date = DateField()

    def get_overview(self):
        return {
            "title": self.title,
            "start_date": self.start_date,
            "offset_emissions_CO2e": self.offset_emissions_CO2e
        }
