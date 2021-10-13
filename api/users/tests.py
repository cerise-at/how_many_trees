from django.contrib.auth import get_user_model
from .serializers import CustomRegisterSerializer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
import json

import pytest
pytestmark = pytest.mark.django_db

from .models import Project

from datetime import date


class TestCustomUserManager(TestCase):

    """
    Tests the creation of the CustomUser model.
    """

    @pytest.mark.django_db
    def test_can_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='foo',
                                        username='username', company='test_company')

        self.assertEqual(user.email, 'test@user.com')
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

        user_creation_args = {
            'email': 'test@user.com', 'password': 'HowManyTrees123',
            'username': 'username', 'company': 'test_company'
        }

        User = get_user_model()
        user = User.objects.create_user(**user_creation_args)
        user_serializer = CustomRegisterSerializer(instance = user)
        data = user_serializer.data

        self.assertEqual(set(data.keys()), set([k for k in user_creation_args.keys() if k != 'password'] + ['emissions_CO2e']))
        self.assertEqual(set(data.values()), set([v for v in user_creation_args.values() if v != 'HowManyTrees123'] + ['0.0000000000']))



class TestDashboardEndpoint(APITestCase):

    """
    Tests the behaviour of the GET /dashboard/?user_email=user@email/ endpoint.
    """

    @pytest.mark.django_db
    def test_dashboard_contains_expected_items(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='test_user', company='test_company')

        self.client.force_authenticate(user=user)
        url = reverse('dashboard', kwargs={'email': user.email})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), user.get_dashboard())



class TestProjectEndpoints(APITestCase):

    """
    Tests the behaviour of the project endpoints:
    * GET projects/id/<project_id>
    * GET projects/user/<email>
    * POST projects/create
    * UPDATE projects/update
    """

    test_data = {
        'company': 'test_company',
        'title': 'Test Project Title',
        'description': 'test description',
        'start_date': date.today(),
        'end_date': date.today(),
        'offset_emissions_CO2e': 125.0
    }

    """
    GET projects/id/<project_id>
    """
    @pytest.mark.django_db
    def test_get_project_id_contains_expected_fields(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='first', company='test_company')

        project = Project.objects.create(**self.test_data)
        url = reverse('project_detail', kwargs={'project_id': project.id})
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content.decode('utf-8'))
        response_keys = set([k for k in data.keys()])
        expected_keys = set([k for k in self.test_data.keys()])
        self.assertEqual(response_keys, expected_keys)

    
    @pytest.mark.django_db
    def test_get_project_id_auth_protected(self):
        # stub
        pass


    """
    GET projects/user/<email>
    """
    @pytest.mark.django_db
    def test_get_user_projects_contains_expected_fields(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='first', company='test_company')

        project = Project.objects.create(**self.test_data)
        url = reverse('user_projects', kwargs={'company': user.company})
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content.decode('utf-8'))
        assert len(data) == 1
        data = data[0]
        response_keys = set([k for k in data.keys()])
        expected_keys = set([k for k in self.test_data.keys()])
        self.assertEqual(response_keys, expected_keys)


    """
    POST projects/create
    """
    @pytest.mark.django_db
    def test_projects_create_correctly_instantiates_project(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='first', company='test_company')

        url = reverse('create_project')
        self.client.force_authenticate(user=user)
        assert len(Project.objects.all()) == 0
        response = self.client.post(url, self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert len(Project.objects.all()) == 1


    """
    UPDATE projects/create
    """
    @pytest.mark.django_db
    def test_projects_update_correctly_updates_project(self):

        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='HowManyTrees123',
                                        username='first', company='test_company')

        project = Project.objects.create(**self.test_data)
        updated_field = { 'offset_emissions_CO2e': 123.4 }

        url = reverse('update_project', kwargs={ 'project_id': project.id })
        self.client.force_authenticate(user=user)
        response = self.client.post(url, updated_field)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



    


    # url('projects/create/', user_views.create_project, name='create_project'),
    # url('projects/update/', user_views.update_project, name='update_project'),