from django.db import models

# Create your models here.
class Car(models.Model):
       
       co2_emissions = models.IntegerField
       revenue_weight = models.IntegerField
       reg_plate = models.CharField(max_length=50)

   #   def __init__(self, data):
   #          self.co2Emissions = data["co2Emissions"]
   #      self.revenueWeight = data["revenueWeight"]
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
       registration= models.CharField(max_length=50),
       car_class= models.CharField(max_length=50),
       emissions= models.IntegerField
    
