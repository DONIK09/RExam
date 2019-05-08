# Create your views here.
from django.shortcuts import render
from django.views import View

from RExamNews.models import RExamNewsModel


class NewsView(View):
    def get(self, request):
        news = RExamNewsModel.objects.all()
        return render(request, 'RExamNews/NewsView.html', context={'news': news})
