from django.shortcuts import render
import requests
from .models import Car
from rest_framework.views import APIView
import pprint


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

            new_vehicle = {'co2_emissions': co2, 'revenue_weight': rev_weight, 'reg_plate': reg}
            return(new_vehicle)

def get_directions_info(request):
      if request.method == 'GET':
            startpoint = 'ba46bn'
            endpoint = 'wolverhampton'
            geo_points = get_lat_long(startpoint, endpoint)
            print(geo_points)

            # headers= { 'alternatives: true', 'origin: {request.orig}', 'destination: {request.dest}'}
            url = f'https://api.mapbox.com/directions/v5/driving{geo_points}'
      
            response = requests.request("POST", url)
            
            data = response.json()
            print(data)
            routes = data['routes']
            if len(routes) <1:
                  one = data["geocoded_waypoints"][0]["place_id"]
                  two = data["geocoded_waypoints"][1]["place_id"]
                  origin = f'place_id:{one}'
                  desintation = f'place_id:{two}'
                  url = f'https://api.mapbox.com/directions/v5/driving'
                  response = requests.request("POST", url)
                  data = response.json()
                  print(data)
           
            return data


def get_lat_long(startpoint, endpoint):
      url_start_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{startpoint}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
      start_response = requests.request('GET', url_start_lat_long)
      start_data = start_response.json()
      coords = start_data['features'][0]['geometry']['coordinates']
      
      url_end_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{endpoint}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
      end_response = requests.request('GET', url_end_lat_long)
      end_data = end_response.json()
      coords.extend(end_data['features'][0]['geometry']['coordinates'])

      return coords


class RouteViews(APIView):
      def get(self, request, format=None):
            
            vehicle = get_vehicle_info(request)
            
            
            route = get_directions_info(request)

           
            return vehicle

      def post(self, request, format=None):
            vehicle = get_vehicle_info(request)
            
            route = get_directions_info(request)
           
           
            return vehicle