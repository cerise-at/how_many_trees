from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from .managers import CustomUserManager
from routes.models import Route

class Project(models.Model):

    company = models.CharField(null=False, unique=True, max_length=255)

    def get_overview(self):
        return {'test': 'success'}


class User(AbstractUser):
    """
    Overwrites the existing django User model.
    * 'Email' as primary key instead of 'username' and used for authentication.
    * 'Company' as new required field.
    """

    username = models.CharField(null=False, max_length=255)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    company = models.CharField(null=False, unique=True, max_length=255)
    emissions_CO2e = models.DecimalField(default=0.0, max_digits=19, decimal_places=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_dashboard(self):

        try:
            routes = [route.get_overview() for route in Route.objects.get(company=self.company)]
        except:
            routes = []

        try:
            projects = [project.get_overview() for project in Project.objects.get(company=self.company)]
        except:
            projects = []

        return { "username": self.username,
                 "company": self.company,
                 "n_trees": f'{self.emissions_CO2e / 7 if self.emissions_CO2e > 0 else 0.0}',
                 "routes": routes, 
                 "projects": projects }

