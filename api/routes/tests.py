from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

client = APIClient()
client.login(username='lauren', password='secret')
# Create your tests here.

"""
test dvla 
test Exception
test lat long
test exception
test map box
test exception
test sending info to the front
test sending errors to the front
test saving to database

"""