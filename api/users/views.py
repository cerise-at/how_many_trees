from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import CustomUser
import json

# Create your views here.
def dashboard(request, user_email):
    print('dashboard received user_email: ', user_email)
    user = get_object_or_404(CustomUser, pk=user_email)
    print(user.get_dashboard())
    # return Response(json.dumps(user.get_dashboard()), content_type='application/json')
    return Response(json.dumps({"status": 200}))