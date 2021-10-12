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
        


# """
# test dvla 
# test Exception
# test lat long
# test exception
# test map box
# test exception
# test sending info to the front
# test sending errors to the front
# test saving to database
# """

# class BaseTestCase(TestCase):

#     @classmethod
#     def mock_dvla(cls):
#         cls.data = {
#             "data": {
#                 {
#                 "artEndDate": "2025-02-28",
#                 "co2Emissions" : 135,
#                 "colour" : "BLUE",
#                 "engineCapacity": 2494,
#                 "fuelType" : "PETROL",
#                 "make" : "ROVER",
#                 "markedForExport" : false,
#                 "monthOfFirstRegistration" : "2004-12",
#                 "motStatus" : "No details held by DVLA",
#                 "registrationNumber" : "ABC1234",
#                 "revenueWeight" : 1640,
#                 "taxDueDate" : "2007-01-01",
#                 "taxStatus" : "Untaxed",
#                 "typeApproval" : "N1",
#                 "wheelplan" : "NON STANDARD",
#                 "yearOfManufacture" : 2004,
#                 "euroStatus": "EURO 6 AD",
#                 "realDrivingEmissions": "1",
#                 "dateOfLastV5CIssued": "2016-12-25"
#                 }
#             }
#         } 

#         return data

#     def mock_routes(cls):
#         cls.routes = {
#             {"routes":[
#                 {"weight_name":"auto",
#                 "weight":10404.483,
#                 "duration":10465.842,
#                 "distance":209123.406,
#                 "legs":[
#                     {"via_waypoints":[],
#                     "admins":[
#                         {"iso_3166_1_alpha3":"GBR","iso_3166_1":"GB"}],
#                         "weight":10404.483,
#                         "duration":10465.842,
#                         "steps":[],
#                         "distance":209123.406,
#                         "summary":"M4, M5"}],
#                         "geometry":
#                         {"coordinates":[[-2.451677,51.140161],[-2.45198,51.139039],[-2.44292,51.147517],[-2.425656,51.14276],[-2.378233,51.200142],[-2.378215,51.200629],[-2.340444,51.211189],[-2.316746,51.208112],[-2.288642,51.24079],[-2.290337,51.243927],[-2.288733,51.255069],[-2.276555,51.262646],[-2.284697,51.270328],[-2.273101,51.282287],[-2.275241,51.285486],[-2.275204,51.285488],[-2.250571,51.347448],[-2.252469,51.34877],[-2.309397,51.402315],[-2.330332,51.396184],[-2.369228,51.453154],[-2.350304,51.501131],[-2.507898,51.505191],[-2.546491,51.544306],[-2.550176,51.548136],[-2.29185,51.796052],[-2.152943,51.875012],[-2.120709,52.020667],[-2.200986,52.129872],[-2.084814,52.335695],[-2.019014,52.425945],[-2.022294,52.488853],[-2.019643,52.492547],[-2.021329,52.492936],[-2.073158,52.522781],[-2.096776,52.551495],[-2.100811,52.554824],[-2.104207,52.575099],[-2.120938,52.583162],[-2.122816,52.583875],[-2.123167,52.584158],[-2.122829,52.585442],[-2.1261,52.584974]],"type":"LineString"}}],
#                         "waypoints":[{"distance":25.197,"name":"Crow's Hill","location":[-2.451677,51.140161]},{"distance":101.905,"name":"Castle Yard","location":[-2.1261,52.584974]}],
#                         "code":"Ok",
#                         "uuid":"gVqgNk5ROkceHnxcsHjGbcsn19HbLEpqkeOo9gz7_RfIEpBCg6xVFw=="}
#         }

#         return routes

#     def mock_request():
#         {
#             "method": 'POST'
#         }


# class TestBasicViews(BaseTestCase):
#     c = Client()

#     def test_dvla(monkeypatch):
#         monkeypatch.setattr(views, "data_request", mock_dvla())
#         data = json.loads(views.get_vehicle_info('registrationNumber', 'co2Emissions', 'revenueWeight'))
#         assert 1640 == data["revenueWeight"]

#     def test_latlong(monkeypatch):
#         monkeypatch.setattr(views, "data_request", mock_routes())
#         data = json.loads(views.get_directions_info('start', 'end'))