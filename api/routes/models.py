from django.db import models

# Create your models here.

class Routes(models.Model):
       route_id = models.IntegerField(primary_key=True),
       route_start = models.IntegerField,
       route_end = models.IntegerField,
       route_dates = models.CharField(max_length=50)
       route_emissions= models.IntegerField,
       duration = models.IntegerField,
       distance = models.IntegerField,
       route_name = models.CharField(max_length=50)
       company_name= models.CharField(max_length=50),
       car_co2_emissions= models.IntegerField,
       revenue_weight = models.IntegerField,
       reg_plate = models.CharField(max_length=50)
    
