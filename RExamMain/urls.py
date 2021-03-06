from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.MainPage.as_view()), name='MainContent')
]
