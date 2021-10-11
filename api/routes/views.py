from django.shortcuts import render
import requests
from .models import Car
from rest_framework.views import APIView


def get_vehicle_info(request):
      
      if request.method == 'GET':
            
            url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

            payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
            headers = { 'x-api-key': 'yaA4ghNltM91GCEFqIjEg6c0ECFJtN12aMhNR1CO','Content-Type': 'application/json' }

            response = requests.request("POST", url, headers=headers, data = payload)
            data = response.json()
            reg = data['registrationNumber']
            co2 = data['co2Emissions']
            rev_weight = data['revenueWeight']

            print(data)
            print(reg)
            print(co2)
            print(rev_weight)
            new_vehicle = Car(co2_emissions = co2, revenue_weight = rev_weight, reg_plate = reg)
            
            return(new_vehicle)

def get_directions_info(request):
      if request.method == 'GET':

class RouteViews(APIView):
      def get(self, request, format=None):
            
            vehicle = get_vehicle_info(request)

           
            return vehicle

      def post(self, request, format=None):
            vehicle = get_vehicle_info(request)
           
            print(vehicle)
            return vehicle