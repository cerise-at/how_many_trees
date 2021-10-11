from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import CustomUser
import json

# Create your views here.
def dashboard(request, user_email):
    # print('dashboard received user_email: ', user_email)
    user = get_object_or_404(CustomUser, pk=user_email)
    return HttpResponse(json.dumps(user.get_dashboard()), content_type='application/json')