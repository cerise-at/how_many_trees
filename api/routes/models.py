from django.db import models
from django.db.models.fields import CharField, DecimalField, EmailField, IntegerField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Route(models.Model):

    company = models.CharField(null=False, unique=True, max_length=255)
    start_address = CharField(null=False, max_length=255)
    end_address = CharField(null=False, max_length=255)
    distance_km = DecimalField(default=0.0, max_digits=19, decimal_places=10)
    coords = ArrayField(models.DecimalField(max_digits=19, decimal_places=10))
    dates = ArrayField(models.DateField(auto_now=True))

    # vehicle details
    vehicle_registration = CharField(null=True, max_length=17)
    vehicle_class = CharField(null=True, max_length=17)
    vehicle_emissions_CO2e_km = IntegerField(default=0)

    def get_overview(self):
        return {'test': 'success'}
