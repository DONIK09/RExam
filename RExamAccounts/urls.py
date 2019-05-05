from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='SignUp'),
    path('signin', views.SignIn.as_view(), name='SignIn'),
    path('signout', views.SignOut.as_view(), name='SignOut'),
    path('profile', views.Profile.as_view(), name="Profile"),
    path('', views.SignIn.as_view())
]
