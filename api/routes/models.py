from django.db import models
from django.db.models.fields import CharField, DecimalField, EmailField


class Route(models.Model):

    email = EmailField(null=False)
    start_address = CharField(null=False, max_length=255)
    end_address = CharField(null=False, max_length=255)
    vehicle_registration = CharField(null=False, max_length=17)
    emissions_CO2e = DecimalField(default=0.0, max_digits=19, decimal_places=10)
    # route_dates = []
    # coords = [[]]

    @classmethod
    def create(cls, **kwargs):
        route = cls(kwargs=kwargs)
        # logic here
        return route

    def __str__(self):
        return f'{self.start_address} to {self.end_address} ({self.vehicle_registration})'