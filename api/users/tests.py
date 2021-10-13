from django.contrib.auth import get_user_model
from .serializers import CustomRegisterSerializer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse

import pytest
pytestmark = pytest.mark.django_db

from .models import Project



# class TestCustomUserManager(TestCase):

#     """
#     Tests the creation of the CustomUser model.
#     """

#     @pytest.mark.django_db
#     def test_can_create_user(self):

#         # Company is currently stub (@OGWJ 09-10-21)
#         User = get_user_model()
#         user = User.objects.create_user(email='test@user.com', password='foo',
#                                         first_name='first', company_name='test_company')

#         self.assertEqual(user.email, 'test@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)

#         try:
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass


#     @pytest.mark.django_db
#     def test_cannot_create_user(self):

#         """
#         Assert cannot create user with any missing field.
#         """

#         User = get_user_model()

#         # NOTE: Cannot parametrize using pytest decorator due to django_db error.
#         failing_params = [(None, 'baz', 'first', 'test_company'),
#                           ('foo@bar.com', None, 'first', 'test_company'),
#                           ('foo@bar.com', 'baz', None, 'test_company'),
#                           ('foo@bar.com', 'baz', 'first', None)]
        
#         with self.assertRaises(ValueError):
#             for e, p, f, s, c in failing_params:
#                 User.objects.create_user(email=e, password=p, first_name=f, company=c)



# class TestCustomerUserSerializer(TestCase):

#     """
#     Tests the behaviour of the CustomUserSerializer.
#     """

#     @pytest.mark.django_db
#     def test_contains_expected_keys_values(self):

#         User = get_user_model()
#         user = User.objects.create_user(email='test@user.com', password='foo',
#                                         first_name='first', company_name='test_company')

#         user_serializer = CustomRegisterSerializer(instance = user)
#         data = user_serializer.data

#         self.assertEqual(set(data.keys()), set(['email', 'password', 'first_name', 'company_name']))
#         self.assertEqual('test@user.com', data['email'])
#         self.assertEqual('first', data['first_name'])



# class TestDashboardEndpoint(APITestCase):

#     """
#     Tests the behaviour of the GET /dashboard/?user_email=user@email/ endpoint.
#     """

#     @pytest.mark.django_db
#     def test_dashboard_contains_expected_fields(self):
#         User = get_user_model()
#         user = User.objects.create_user(email='test@user.com', password='foo',
#                                         first_name='first', company_name='test_company')

#         url = reverse('dashboard', kwargs={'user_email': user.email})

#         # NOTE: stubbed response!
#         expected_response = {
#             "first_name": user.first_name,
#             "company_name": user.company_name,
#             "n_trees": f'{user.emissions_CO2e / 7}',
#             "routes": [
#                 {
#                     "start_address": "address",
#                     "stop_address": "address",
#                     "emissions_CO2e": 100,
#                     "distance_km": 100,
#                     "vehicle_registration": "SA65 XXX"
#                 }
#             ],
#             "projects": [
#                 {
#                     "project_title": "Project Title Placeholder",
#                     "project_description": "Project Description Placeholder"
#                 }
#             ]
#         }

#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), expected_response)

from datetime import date

class TestGetProjectEndpoint(APITestCase):

    """
    Tests the behaviour of the GET /dashboard/?user_email=user@email/ endpoint.
    """

    test_data = {
        'id': 0,
        'title': 'Test Project Title',
        'description': 'test description',
        'start_date': date.today(),
        'end_date': date.today() 
    }

    @pytest.mark.django_db
    def test_get_project_contains_expected_fields(self):

        # project = Project.objects.create(**self.test_data)
        url = reverse('project_detail', kwargs={'project_id': 0})

        print(url)

        unauth_response = self.client.get(url)
        self.assertEqual(unauth_response.status_code, status.HTTP_401_UNAUTHORIZED)

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='first', company='test_company')

        # token = Token.objects.get(user__username='lauren')
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.client.force_authenticate(user=user)
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.status_code, status.HTTP_200_OK)

