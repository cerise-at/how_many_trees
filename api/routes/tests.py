from django.test import TestCase
import pytest
from .models import Route
# from numpy import repeat
from django.db.utils import IntegrityError

# Create your tests here.
class TestRouteModel(TestCase):

    """
    Tests the behaviour of the Route model.
    * test_model_created
    * test_model_not_created
    """

    test_data = {
        "email": "user@email.test", 
        "start_address": "34 Test Street, The Town, The County, The Country",
        "end_address": "35 Test Street, The Town, The County, The Country",
        "vehicle_registration": "XXXX XXXX",
        "emissions_CO2e": 0
    }

    @pytest.mark.django_db
    def test_model_created(self):

        """
        Test that Route model is successfully created and stores 
        all field values passed to the constructor.
        """

        route = Route.objects.create(**self.test_data)
        for key, value in self.test_data.items():
            assert route.__dict__[key] == value
        return


    def generate_missing_value_cases(self, kwargs):

        """
        Generate a list of dict copies with one value missing in every copy.
        """

        retval = []
        for i in range(len(kwargs.keys())):
            retval.append({**kwargs})
      
        for i, case in enumerate(retval):
            for j, key in enumerate(case.keys()):
                if i == j:
                    case[key] = None
                    break
        return retval 


    def test_model_not_created(self):

        """
        Test that Route model is not successfully created with any missing fields.
        """

        with self.assertRaises(IntegrityError):
            for kwargs in self.generate_missing_value_cases(self.test_data):
                Route.objects.create(**kwargs)

        return