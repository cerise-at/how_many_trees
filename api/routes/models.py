from django.db import models

# Create your models here.
class Car(models.Model):
     def __init__(self, data):
        self.co2Emissions = data["co2Emissions"]
        self.revenueWeight = data["revenueWeight"]