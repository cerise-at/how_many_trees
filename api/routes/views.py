from django.shortcuts import render
import requests
from .models import Routes
from rest_framework.views import APIView


def calc_emissions(distance, vehicle):
      if vehicle['revenue_weight'] == 0:
            route_emissions = vehicle['co2_emissions']*distance
            return route_emissions
      else:
            emissions = vehicle['co2_emissions']
            rev_weight = vehicle['revenue_weight']
            route_emissions = (distance*emissions)*rev_weight
            return route_emissions

def get_vehicle_info(request):
      if request.method == 'GET':
            reg = request.GET['reg']
            url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
            payload = "{\n\t\"registrationNumber\": \"{reg}\"\n}"
            headers = { 'x-api-key': 'yaA4ghNltM91GCEFqIjEg6c0ECFJtN12aMhNR1CO','Content-Type': 'application/json' }
            response = requests.request("POST", url, headers=headers, data = payload)
            if response == 200:
                  data = response.json()
                  reg = data['registrationNumber']
                  co2 = data['co2Emissions']
                  rev_weight = data['revenueWeight']
                  new_vehicle = {'co2_emissions': co2, 'revenue_weight': rev_weight, 'reg_plate': reg}
                  return(new_vehicle)
            else:
                  new_vehicle = {'co2_emissions': calc_emissions_no_vehicle_info(), 'revenue_weight': 0, 'reg_plate': 'unknown'}
                  

def get_lat_long(startpoint, endpoint):
      try:
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
      except Exception as e:
            return  (e)


def calc_emissions_no_vehicle_info():
      total_emits_per_km = (100000 * 500 * 62)/1000000
      return total_emits_per_km


def get_directions_info(request):
      if request.method == 'GET':
            startpoint = request.GET['start']
            endpoint = request.GET['end']
            coords = get_lat_long(startpoint, endpoint)
      
            url = f'https://api.mapbox.com/directions/v5/mapbox/driving/{coords}?geometries=geojson&alternatives=true&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1ycG54cDBkZ3MzMW9hYjY4dnAwNXMifQ.gsFC-xmHmsp-EneBn8yrQQ'
            try:
                  response = requests.request("GET", url)
                  data = response.json()
                  data = data['routes']
                  return(data)
            except Exception as e:
                  return e



class Directions(APIView):    
      def get(self, request, format=None):
            if request.method =='GET':
                  if request.GET['vehicle_registration']:
                        vehicle = get_vehicle_info(request)
                        routes = get_directions_info(request, vehicle, package_weight=200)
                        for route in routes:
                              routes.append(
                              {'distance': route['distance'], 'duration': round(route['duration']/3600, 2), 'coordinates': route['geometry']['coordinates'], 'emissions': calc_emissions(route['distance'], vehicle)})
                        return {'routes': routes}
                  elif request.GET['vehicle_class']:
                        routes = get_directions_info(request, package_weight=20)
                        for route in routes:
                              routes.append(
                              {'distance': route['distance'], 'duration': round(route['duration']/3600, 2), 'coordinates': route['geometry']['coordinates'], 'emissions': (calc_emissions_no_vehicle_info()*route['distance'])})
                        return {'routes': routes}
                  else:
                        return ("Not enough information provided, please try again")
            elif request.method =='POST':
                  new_route = Routes(request)  
                  new_route.save()    