from django.shortcuts import render
# Create your views here.
from django.views import View


class MainPage(View):
    def get(self, request):
        user = request.user
        return render(request, 'RExamMain/EmptyView.html', context={'user': user})
