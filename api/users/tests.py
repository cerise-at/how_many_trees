import pytest
from django.contrib.auth import get_user_model
from .models import Company
from django.test import TestCase

pytestmark = pytest.mark.django_db


class UsersManagersTests(TestCase):


    @pytest.mark.django_db
    def test_can_create_user(self):

        test_company = Company.objects.create()
        User = get_user_model()

        # Company is currently stub (@OGWJ 09-10-21)
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
        NOTE: Nested function definition required to allow both parametrize and django-db access decorators. 
        """

        test_company = Company.objects.create()
        User = get_user_model()

        failing_user_creation_test_cases = [(None, 'baz', 'first', 'last', test_company),
                                            ('foo@bar.com', None, 'first', 'last', test_company),
                                            ('foo@bar.com', 'baz', None, 'last', test_company),
                                            ('foo@bar.com', 'baz', 'first', None, test_company),
                                            ('foo@bar.com', 'baz', 'first', 'last', None)]

        @pytest.mark.parametrize("email, password, first_name, surname, company", failing_user_creation_test_cases)
        def test_failing_cases(self, email, password, first_name, surname, company):
            with self.assertRaises(TypeError):
                User.objects.create_user(email=email, password=password, first_name=first_name, surname=surname, company=company)