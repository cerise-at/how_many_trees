from django.shortcuts import render
import requests
from .models import Car


def get_vehicle_info(request):
      
      if request.method == 'GET':
            
            url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

            payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
            headers = { 'x-api-key': 'yaA4ghNltM91GCEFqIjEg6c0ECFJtN12aMhNR1CO','Content-Type': 'application/json' }

            response = requests.request("POST", url, headers=headers, data = payload)
            reg = response[0].text.encode('utf8')
            co2 = response[11].text.encode('utf8')
            rev_weight = response[17].text.encode('utf8')

            print(response.text.encode('utf8'))
            new_vehicle = Car(co2_emissions = co2, revenue_weight = rev_weight, reg_plate = reg)
            new_vehicle.save()



