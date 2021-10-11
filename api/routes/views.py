from django.shortcuts import render

# Create your views here.
# def data_request(registrationNumber, co2Emissions, revenueWeight):
#     url = f"https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles?registrationNumber={registrationNumber}&co2Emissions={co2Emissions}&revenueWeight={revenueWeight}&key=4374ac90-b6ff-4b8c-a86e-809564970414"
#     resp = requests.get(url)
#     return resp.json()

import requests

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
headers = {
  'x-api-key': '4374ac90-b6ff-4b8c-a86e-809564970414',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

def get_vehicle_info():{

}

def get_route_info():{

}

def return_cotwo_info():{
  
}