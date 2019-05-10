# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from RExamNews.models import RExamNewsModel


class NewsView(View):
    def get(self, request):
        if request.is_ajax():
            news_list = RExamNewsModel.objects.all().order_by('-id')
            paginator = Paginator(news_list, 6)

            page = request.GET.get('page')
            try:
                news = paginator.page(page)
            except PageNotAnInteger:
                news = paginator.page(1)
            except EmptyPage:
                news = paginator.page(paginator.num_pages)

            return render(request, 'RExamNews/NewsView.html', context={'news': news})
        return HttpResponseNotFound
