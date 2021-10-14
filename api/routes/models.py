from django.db import models
from django.db.models.fields import CharField, DecimalField, EmailField, IntegerField
from django.contrib.postgres.fields import ArrayField


class Route(models.Model):

   name = CharField(null=False, max_length=255)
   start_address = CharField(null=False, max_length=255)
   email = EmailField(null=False)
   end_address = CharField(null=False, max_length=255)
   distance_km = DecimalField(default=0.0, max_digits=40, decimal_places=20)
   coords = ArrayField(models.DecimalField(max_digits=40, decimal_places=20))
   dates = ArrayField(models.DateField(auto_now=True)),
   emissions = DecimalField(default=0.0, max_digits=40, decimal_places=20)

   # vehicle details
   vehicle_registration = CharField(null=True, max_length=17)
   vehicle_class = CharField(null=True, max_length=17)
   vehicle_emissions_CO2e_km = DecimalField(default=0.0, max_digits=40, decimal_places=20)

   @classmethod
   def create(cls, **kwargs):
        route = cls(kwargs=kwargs)
        # logic here
        return route

   def get_overview(self):
         return {
            'id': self.id,
            'name': self.name,
            'distance_km': str(self.distance_km),
            'emissions_CO2e': str(self.emissions),
            'emissions_CO2e_km': str(self.vehicle_emissions_CO2e_km)
         }

   def __str__(self):
      return f'{self.start_address} to {self.end_address} ({self.vehicle_registration})'
