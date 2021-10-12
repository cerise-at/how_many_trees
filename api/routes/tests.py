from django.test import TestCase

# Create your tests here.
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

def mock_dvla(a, b, c):
    data = {
        "data": {
            {
            "artEndDate": "2025-02-28",
            "co2Emissions" : 135,
            "colour" : "BLUE",
            "engineCapacity": 2494,
            "fuelType" : "PETROL",
            "make" : "ROVER",
            "markedForExport" : false,
            "monthOfFirstRegistration" : "2004-12",
            "motStatus" : "No details held by DVLA",
            "registrationNumber" : "ABC1234",
            "revenueWeight" : 1640,
            "taxDueDate" : "2007-01-01",
            "taxStatus" : "Untaxed",
            "typeApproval" : "N1",
            "wheelplan" : "NON STANDARD",
            "yearOfManufacture" : 2004,
            "euroStatus": "EURO 6 AD",
            "realDrivingEmissions": "1",
            "dateOfLastV5CIssued": "2016-12-25"
            }
        }
    } 

    return data

def mock_request():
    {
        "method": 'POST'
    }

def test_dvla(monkeypatch):
    monkeypatch.setattr(views, "data_request", mock_dvla())
    data = json.loads(views.get_vehicle_info('registrationNumber', 'co2Emissions', 'revenueWeight'))
    assert 1640 == data["revenueWeight"]
