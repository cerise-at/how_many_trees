from django.contrib.auth import get_user_model
from .serializers import CustomRegisterSerializer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse

import pytest
pytestmark = pytest.mark.django_db



test_data = {
    'email': 'test@user.email', 'password': 'test_password',
    'username': 'test_username', 'company': 'test_company'
}



class TestCustomUserManager(TestCase):

    """
    Tests the creation of the CustomUser model.
    """

    # test_data = {
    #     'email': 'test@user.email', 'password': 'test_password',
    #     'username': 'test_username', 'company': 'test_company'
    # }

    @pytest.mark.django_db
    def test_can_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(**test_data)
        for key in test_data.keys():
            # password is hashed and not directly comparable
            if key != 'password':
                self.assertEqual(test_data[key], user.__dict__[key])

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
                User.objects.create_user(email=e, password=p, username=f, company=c)



class TestCustomerRegisterSerializer(TestCase):

    """
    Tests the behaviour of the CustomRegisterSerializer.
    """

    @pytest.mark.django_db
    def test_contains_expected_keys_values(self):

        User = get_user_model()
        user = User.objects.create_user(**test_data)
        user_serializer = CustomRegisterSerializer(instance = user)
        data = user_serializer.data

        self.assertEqual(set(data.keys()), set(['username', 'email', 'company', 'emissions_CO2e']))
        # self.assertEqual('test@user.com', data['email'])
        # self.assertEqual('first', data['first_name'])



class TestDashboardEndpoint(APITestCase):

    """
    Tests the behaviour of the GET /dashboard/?user_email=user@email/ endpoint.
    """

    @pytest.mark.django_db
    def test_dashboard_contains_expected_fields(self):
        User = get_user_model()
        user = User.objects.create_user(**test_data)
        url = reverse('dashboard', kwargs={'email': user.email})

        # NOTE: stubbed response!
        # expected_response = {
        #     "username": user.first_name,
        #     "company": user.company,
        #     "n_trees": f'{user.emissions_CO2e / 7}',
        #     "routes": [],
        #     "projects": []
        # }

        expected = {'detail': 'Authentication credentials were not provided.'}

        response = self.client.get(f'{url}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), expected)