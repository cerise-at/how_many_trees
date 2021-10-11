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
            orig = 'london'
            dest = 'taunton'
            # headers= { 'alternatives: true', 'origin: {request.orig}', 'destination: {request.dest}'}
            url = f'https://maps.googleapis.com/maps/api/directions/json?origin={orig}&destination={dest}&key=AIzaSyD6BIsAm5df2OUZ84T3gUb--CrJ8sYu6vE'
      
            response = requests.request("POST", url)
            
            data = response.json()
            routes = data['routes']
            if len(routes) <1:
                  one = data["geocoded_waypoints"][0]["place_id"]
                  two = data["geocoded_waypoints"][1]["place_id"]
                  origin = f'place_id:{one}'
                  desintation = f'place_id:{two}'
                  url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={desintation}&key=AIzaSyD6BIsAm5df2OUZ84T3gUb--CrJ8sYu6vE'
                  response = requests.request("POST", url)
                  data = response.json()
                  print(data)
           
            return data

class RouteViews(APIView):
      def get(self, request, format=None):
            
            vehicle = get_vehicle_info(request)
            
            
            route = get_directions_info(request)

           
            return vehicle

      def post(self, request, format=None):
            vehicle = get_vehicle_info(request)
            
            route = get_directions_info(request)
           
           
            return vehicle