from django.contrib.auth import get_user_model
from .models import Company
from django.test import TestCase

import pytest
pytestmark = pytest.mark.django_db

"""
Tests the creation of the CustomUser model.
"""

class TestCustomUserManager(TestCase):

    @pytest.mark.django_db
    def test_can_create_user(self):

        # Company is currently stub (@OGWJ 09-10-21)
        test_company = Company.objects.create()
        User = get_user_model()
        user = User.objects.create_user(email='test@user.com', password='foo',
                                        first_name='first', surname='last',
                                        company=test_company)

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

        test_company = Company.objects.create()
        User = get_user_model()

        # NOTE: Cannot parametrize using pytest decorator due to django_db error.
        failing_params = [#(None, 'baz', 'first', 'last', test_company),
                          ('foo@bar.com', None, 'first', 'last', test_company),
                          ('foo@bar.com', 'baz', None, 'last', test_company),
                          ('foo@bar.com', 'baz', 'first', None, test_company),
                          ('foo@bar.com', 'baz', 'first', 'last', None)]
        
        with self.assertRaises(TypeError):
            for e, p, f, s, c in failing_params:
                User.objects.create_user(email=e, password=p, first_name=f, surname=s, company=c)