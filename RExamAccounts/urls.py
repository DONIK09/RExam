from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='SignUp'),
    path('signin', views.SignIn.as_view(), name='SignIn'),
    path('signout', login_required(views.SignOut.as_view()), name='SignOut'),
    path('profile', login_required(views.Profile.as_view()), name="Profile"),
    path('', views.SignIn.as_view())
]
