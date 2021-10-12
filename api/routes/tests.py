from django.test import TestCase
import pytest
from .models import Route
from .serializers import RouteSerializer
# from numpy import repeat
from django.db.utils import IntegrityError

# Create your tests here.
class TestRouteModel(TestCase):

    """
    Tests the behaviour of the Route model.
    * test_model_created (and stores correct key value pairs)
    * test_model_not_created (if given missing fields)
    * test_serializes_expected_key_values
    """

    test_data = {
        "email": "user@email.test", 
        "start_address": "34 Test Street, The Town, The County, The Country",
        "end_address": "35 Test Street, The Town, The County, The Country",
        "distance_km": 100,
        "vehicle_registration": "XXXX XXXX",
        "vehicle_class": "HGV",
        "vehicle_emissions_CO2e_km": 0
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


    @pytest.mark.django_db
    def test_serializes_expected_keys_values(self):

        """
        Tests the behaviour of the RouteSerializer.
        """

        route = Route.objects.create(**self.test_data)
        route_serializer = RouteSerializer(instance = route)
        data = route_serializer.data

        self.assertEqual(set(data.keys()), set(self.test_data.keys()))
