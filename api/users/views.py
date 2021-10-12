from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request, email):
    # print('dashboard received user_email: ', user_email)
    user = get_object_or_404(User, email=email)
    return HttpResponse(json.dumps(user.get_dashboard()), content_type='application/json')