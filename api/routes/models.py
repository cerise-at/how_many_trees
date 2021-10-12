from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Route(models.Model):

    company = models.CharField(null=False, unique=True, max_length=255)

    def get_overview(self):
        return {'test': 'success'}
