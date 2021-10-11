from django.shortcuts import get_object_or_404
from .models import CustomUser

# Create your views here.
def dashboard(request, user_email):
    user = get_object_or_404(CustomUser, pk=user_email)
    return user.get_dashboard(), 200