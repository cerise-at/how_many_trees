"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # –––––––––––––––––– AUTH ––––––––––––––––––– #
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    # ––––––––––––––––– ROUTES –––––––––––––––––– #
    path('routes/', include('routes.urls')),
    # –––––––––––––––– PROJECTS ––––––––––––––––– #
    url(r'^projects/id/(?P<project_id>\d+)', user_views.project_detail, name='project_detail'),
    url('projects/create/', user_views.create_project, name='create_project'),
    url('projects/update/', user_views.update_project, name='update_project'),
    url(r'^projects/user/(?P<company>.*)', user_views.get_user_projects, name='user_projects'),
    # –––––––––––––––– DASHBOARD –––––––––––––––– #
    url(r'^dashboard/(?P<email>.*)', user_views.dashboard, name='dashboard')
]