from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Stub
class Company(models.Model):
    pass


class CustomUser(AbstractUser):
    """
    Overwrites the existing django User model.
    * Remove 'username' field/
    * Add 'first_name' and 'surname' required fields.
    * 'Email' as primary key instead of 'username' and used for authentication.
    * 'Company' as new required field.
    """

    username = None
    first_name = models.CharField(null=False, max_length=255)
    surname = models.CharField(null=False, max_length=255)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
