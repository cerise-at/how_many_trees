from django.db import models
from django.db.models.fields import CharField, DecimalField, EmailField



class Route(models.Model):

    email = EmailField(null=False)
    start_address = CharField(null=False, max_length=255)
    end_address = CharField(null=False, max_length=255)
    distance_km = DecimalField(default=0.0, max_digits=19, decimal_places=10)
    # TODO: coords = [] => migrate to postgres for ArrayField?
    # TODO: dates = [] => migrate to postgres for ArrayField?

    # vehicle details
    vehicle_registration = CharField(null=False, max_length=17)
    vehicle_emissions_CO2e_km = CharField(null=False, max_length=17)

    @classmethod
    def create(cls, **kwargs):
        route = cls(kwargs=kwargs)
        # logic here
        return route

    def __str__(self):
        return f'{self.start_address} to {self.end_address} ({self.vehicle_registration})'