from django.contrib.auth.decorators import login_required
from django.urls import path

from RExamNews import views

urlpatterns = [
    path('', login_required(views.NewsView.as_view()), name='News')
]
