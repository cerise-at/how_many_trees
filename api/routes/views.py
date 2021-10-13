from django.shortcuts import render
import requests
from .models import Route
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Calculates the vehicle emissions for a given distance
def calc_emissions(distance, vehicle):
      if vehicle['revenue_weight'] == 0:
            route_emissions = vehicle['co2_emissions']*distance
            return route_emissions
      else:
            emissions = vehicle['co2_emissions'] # gives emissions in g per km
            rev_weight = vehicle['revenue_weight'] # gives weight in kg
            rev_weight_ton = rev_weight/1000 # converts weights to metric tonnes. Revenue weight acts like an emissions "modifier"
            emission_g = (distance*emissions)*rev_weight_ton # gives route emissions in g for freight of that weight transported across the distance moved 
            route_emissions = emission_g/1000000 # converts route emissions to metric tonnes
            return route_emissions 

# This reaches into the DVLA API to get a vehicles registration number, vehicle weight, and CO2 emissions per km. 
def get_vehicle_info(reg, request):
      if request.method == 'GET':
            
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
                  
# This reaches into the MapBox API to get a routes startpoint and endpoint
def get_lat_long(to, fro):
      try:  
            url_start_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{to}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
            start_response = requests.request('GET', url_start_lat_long)
            start_data = start_response.json()
            start = start_data['features'][0]['geometry']['coordinates']
            
            url_end_lat_long = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{fro}.json?country=gb&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1wMWhhaTAxMjAydWp0YnExa2lsanAifQ.11WeE94rbtUkNefoue_dSQ'
            end_response = requests.request('GET', url_end_lat_long)
            end_data = end_response.json()
            end = (end_data['features'][0]['geometry']['coordinates'])
            coords = f"{start[0]},{start[1]};{end[0]},{end[1]}"
            return coords
      except Exception as e:
            return  (e)

# Calculates the vehicle emissions for a given distance if vehicle information is unknown. Uses average for road freight provided by the European Automobile Manufacturers Association
def calc_emissions_no_vehicle_info(distance):
      total_emits_per_km = (26 * distance * 62)/1000000
      return total_emits_per_km

# This reaches into the MapBox API and uses the previously inputted coordinate data to provide a list of routes
def get_directions_info(request, to, fro):
      if request.method == 'GET':
            
            coords = get_lat_long(to, fro)
      
            url = f'https://api.mapbox.com/directions/v5/mapbox/driving/{coords}?geometries=geojson&alternatives=true&access_token=pk.eyJ1IjoiY2VyaXNlLWF0IiwiYSI6ImNrdW1ycG54cDBkZ3MzMW9hYjY4dnAwNXMifQ.gsFC-xmHmsp-EneBn8yrQQ'
            try:
                  response = requests.request("GET", url)
                  data = response.json()
                  data = data['routes']
                  return(data)
            except Exception as e:
                  return e


# Putting it all together: 
# We get our vehicle registration, journey startpoint and journey endpoint from the user. 
# We reach into the DVLA API and, assuming its a valid vehicle registration, get the infor specified in the get_vehicle_info function
# We reach into the MapBox API and get the info on the users startpoint, and endpoint, as well as:
# -- the various routes they can use to get there; 
# -- how long each will take; 
# -- and the distance they'll travel
# We then run our emissions calculations and tell the user how much CO2, in metric tons, their journey/delivery will emit
# If they haven't provided enough information to do this, then it'll throw an error and ask for more information
class Directions(APIView):    
      permission_classes = [IsAuthenticated]
      def get(self, request, format=None):
            if request.method =='GET':
                  if self.request.query_params.get['vehicle_registration']:
                        vehicle = get_vehicle_info(self.request.query_params.get['vehicle_registration'], request)
                        to = self.request.query_params.get['address1']
                        fro = self.request.query_params.get['address2']
                        routes = get_directions_info(request, to, fro)
                        for route in routes:
                              routes.append(
                              {'distance': route['distance'], 'duration': round(route['duration']/3600, 2), 'coordinates': route['geometry']['coordinates'], 'emissions': calc_emissions(route['distance'], vehicle)})
                        return {'routes': routes}
                  elif self.request.query_params.get['vehicle_class']:
                        to = self.request.query_params.get['address1']
                        fro = self.request.query_params.get['address2']
                        routes = get_directions_info(request, to, fro)
                        for route in routes:
                              routes.append(
                              {'distance': route['distance'], 'duration': round(route['duration']/3600, 2), 'coordinates': route['geometry']['coordinates'], 'emissions': (calc_emissions_no_vehicle_info()*route['distance'])})
                        return {'routes': routes}
                  else:
                        return ("Not enough information provided, please try again")
            elif request.method =='POST':
                  new_route = Route.create(request)  
                      