from django.db import models

# Create your models here.
class Car(models.Model):
       
       co2_emissions = models.IntegerField(max_length=50)
       revenue_weight = models.IntegerField(max_length=50)
       reg_plate = models.CharField(max_length=50)

   #   def __init__(self, data):
   #          self.co2Emissions = data["co2Emissions"]
   #      self.revenueWeight = data["revenueWeight"]