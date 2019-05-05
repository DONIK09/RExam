from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainPage(View):
    def get(self, request):
        user = request.user
        return render(request, 'RExamMain/EmptyView.html', context={'user': user})


class MainContent(View):
    def get(self, request):
        if request.is_ajax():
            return render(request, 'RExamMain/MainView.html')
        return HttpResponseNotFound
