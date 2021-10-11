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

def get_directions_info(request, vehicle):
      if request.method == 'GET':
            startpoint = 'ba46bn'
            endpoint = 'wolverhampton'
            coords = get_lat_long(startpoint, endpoint)
            print(coords)

            # headers= { 'alternatives: true', 'origin: {request.orig}', 'destination: {request.dest}'}
            url = f'https://api.mapbox.com/directions/v5/mapbox/driving/{coords}?geometries=geojson&alternatives=true&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1ycG54cDBkZ3MzMW9hYjY4dnAwNXMifQ.gsFC-xmHmsp-EneBn8yrQQ'
      
            response = requests.request("GET", url)
            data = response.json()
            data = data['routes']
           
            routes= {}
            for route in range(len(data)):
                  routes[route] = {}
                  for item in data:
                        routes[route]['distance'] = item['distance']/1000
                        routes[route]['duration'] = round(item['duration']/3600, 2)
                        routes[route]['coordinates'] = item['geometry']['coordinates']
                        routes[route]['emissions'] = calc_emissions(item['distance'], vehicle['co2_emissions'])

            return(routes)


def get_lat_long(startpoint, endpoint):
      url_start_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{startpoint}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
      start_response = requests.request('GET', url_start_lat_long)
      start_data = start_response.json()
      start = start_data['features'][0]['geometry']['coordinates']
      
      
      url_end_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{endpoint}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
      end_response = requests.request('GET', url_end_lat_long)
      end_data = end_response.json()
      end = (end_data['features'][0]['geometry']['coordinates'])
      coords = f"{start[0]},{start[1]};{end[0]},{end[1]}"
      return coords

def calc_emissions(distance, emissions):
      

      return 

class RouteViews(APIView):
      def get(self, request, format=None):
            
            vehicle = get_vehicle_info(request)
            
            routes = get_directions_info(request, vehicle)


           
            return vehicle

      def post(self, request, format=None):
            vehicle = get_vehicle_info(request)
            
            route = get_directions_info(request)
           
           
            return vehicle