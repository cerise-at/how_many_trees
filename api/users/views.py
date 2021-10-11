from django.shortcuts import get_object_or_404
from .models import CustomUser

# Create your views here.
def dashboard(request, user_email):
    user = get_object_or_404(CustomUser, pk=user_email)
    # user_dashboard = {
    #     "first_name": "test name",
    #     "company_name": "test company",
    #     "n_trees": 100,
    #     "routes": [
    #         {
    #             "start_address": "address 1",
    #             "stop_address": "address 2",
    #             "emissions_CO2e": 100,
    #             "distance_km": 1000,
    #             "vehicle_registration": "SA65 XXX"
    #         }
    #     ]
    # }
    return user.get_dashboard(), 200