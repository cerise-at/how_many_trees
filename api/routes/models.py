from django.db import models

# Create your models here.
class Car(models.Model):
       
       co2_emissions = models.IntegerField
       revenue_weight = models.IntegerField
       reg_plate = models.CharField(max_length=50)

   #   def __init__(self, data):
   #          self.co2Emissions = data["co2Emissions"]
   #      self.revenueWeight = data["revenueWeight"]