from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.authtoken.models import Token
from django.urls import reverse

import pytest
pytestmark = pytest.mark.django_db



class TestCustomUserManager(TestCase):

    """
    Tests the creation of the CustomUser model.
    """

    @pytest.mark.django_db
    def test_can_create_user(self):

        # Company is currently stub (@OGWJ 09-10-21)
        User = get_user_model()
        user = User.objects.create_user('test@user.com', 'foo',
                                        'first', 'test_company')

        self.assertEqual(user.email, 'test@user.com')
        self.assertEqual(user.username, 'first')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    @pytest.mark.django_db
    def test_cannot_create_user(self):

        """
        Assert cannot create user with any missing field.
        """

        User = get_user_model()

        # NOTE: Cannot parametrize using pytest decorator due to django_db error.
        failing_params = [(None, 'baz', 'first', 'test_company'),
                          ('foo@bar.com', None, 'first', 'test_company'),
                          ('foo@bar.com', 'baz', None, 'test_company'),
                          ('foo@bar.com', 'baz', 'first', None)]
        
        with self.assertRaises(ValueError):
            for e, p, f, s, c in failing_params:
                User.objects.create_user(email=e, password=p, first_name=f, company=c)



class TestCustomerUserSerializer(TestCase):

    """
    Tests the behaviour of the CustomUserSerializer.
    """

    @pytest.mark.django_db
    def test_contains_expected_keys_values(self):

        User = get_user_model()
        user = User.objects.create_user('test@user.com', 'foo',
                                        'first', 'test_company')

        user_serializer = UserSerializer(instance = user)
        data = user_serializer.data

        self.assertEqual(set(data.keys()), set(['email', 'username', 'company']))
        self.assertEqual('test@user.com', data['email'])
        self.assertEqual('first', data['username'])



class TestDashboardEndpoint(APITestCase):

    """
    Tests the behaviour of the GET /dashboard/?user_email=user@email/ endpoint.
    """

    @pytest.mark.django_db
    def test_dashboard_contains_expected_fields(self):
        # commented deliberately => TODO: implement token handing in test.
        return 
        User = get_user_model()
        user = User.objects.create_user('test@user.com', 'HowManyTrees123',
                                        'first', 'test_company')

        url = reverse('dashboard', kwargs={'user_email': user.email})

        # NOTE: stubbed response!
        expected_response = {
            "username": '',#user.name,
            "company": '',#user.company,
            "n_trees": f'{user.emissions_CO2e / 7}',
            "routes": [
                {
                    "start_address": "address",
                    "stop_address": "address",
                    "emissions_CO2e": 100,
                    "distance_km": 100,
                    "vehicle_registration": "SA65 XXX"
                }
            ],
            "projects": [
                {
                    "project_title": "Project Title Placeholder",
                    "project_description": "Project Description Placeholder"
                }
            ]
        }

        self.client.login(username='test@user.com', password='HowManyTrees123')
        token = Token.objects.get(user__username='test@user.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_response)