from django.contrib.auth import get_user_model
from .models import Company
from .serializers import CustomUserSerializer
from django.test import TestCase

import pytest
pytestmark = pytest.mark.django_db



class TestCustomUserManager(TestCase):

    """
    Tests the creation of the CustomUser model.
    """

    @pytest.mark.django_db
    def test_can_create_user(self):

        # Company is currently stub (@OGWJ 09-10-21)
        test_company = Company.objects.create()
        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='foo',
                                        first_name='first', company_name='test_company')

        self.assertEqual(user.email, 'test@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass


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
        user = User.objects.create_user(email='test@user.com', password='foo',
                                        first_name='first', company_name='test_company')

        user_serializer = CustomUserSerializer(instance = user)
        data = user_serializer.data

        self.assertEqual(set(data.keys()), set(['email', 'password', 'first_name', 'company_name']))
        self.assertEqual('test@user.com', data['email'])
        self.assertEqual('first', data['first_name'])