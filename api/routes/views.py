from django.shortcuts import render
import requests

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
headers = {
  'x-api-key': '4374ac90-b6ff-4b8c-a86e-809564970414',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

# class caluate_freight(Resource):
#     def get(self):
#         return {'Message': 'Sucesss', 'data': 'dummy_data' + ' C02'}

#     def put(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('miles', type=float)
#         parser.add_argument('km', type=float)
#         parser.add_argument('tonnes', type=float)
#         parser.add_argument('km/tonnes', type=float)
#         parser.add_argument('miles/tonnes', type=float)
#         args = parser.parse_args()
#         print(args['miles'])
#         print(args['km'])
#         print(args['tonnes'])
#         print(args['km/tonnes'])
#         print(args['miles/tonnes'])

#         if args['miles'] is not None:
#             args['km'] = args['miles'] / 0.621371
#             args['km/tonnes'] = args['km'] * args['tonnes']

#         if args['miles/tonnes'] is not None:
#             args['km/tonnes'] = args['miles/tonnes'] * 1.459972

#         if args['km/tonnes'] is None:
#             args['km/tonnes'] = args['km'] * args['tonnes']

#         g_CO2_tonne_km = args['km/tonnes'] * 8
#         print("g_CO2_tonne_km", g_CO2_tonne_km)
#         metric_tons = g_CO2_tonne_km / 1000000
#         Emmisons = round(metric_tons, 2)

#         calculations = {'Emmisons': str(Emmisons) + ' tonnes of CO2'}

#         return calculations, 201