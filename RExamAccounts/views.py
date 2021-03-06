from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from RExamAccounts.forms import SignUpForm, SignInForm, ProfileEdit
from RExamAccounts.models import StudyGroup


class SignUp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('MainContent')
        study_groups = StudyGroup.objects.all()
        form = SignUpForm
        return render(request, 'RExamAccounts/SignUpView.html', context={'groups': study_groups, 'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('MainContent')
        bounded_form = SignUpForm(request.POST)
        if bounded_form.is_valid():
            new_user = bounded_form.save()
            return redirect('RExamAccounts:SignIn')
        else:
            return render(request, 'RExamAccounts/SignUpView.html', context={'form': bounded_form})


class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('MainContent')
        form = SignInForm
        return render(request, 'RExamAccounts/SignInView.html', context={'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        bound_form = SignInForm(request.POST)
        if bound_form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('MainContent')
            else:
                error = 'Введен не правильный логин или пароль!'
                return render(request, 'RExamAccounts/SignInView.html', context={'form': bound_form, 'error': error})
        else:
            return render(request, 'RExamAccounts/SignInView.html', context={'form': bound_form})


class SignOut(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('RExamAccounts:SignIn')
        else:
            return redirect('RExamAccounts:SignIn')


class Profile(View):
    def get(self, request):
        if request.is_ajax():
            form = ProfileEdit(instance=request.user)
            return render(request, 'RExamAccounts/ProfileView.html',
                          context={'form': form, 'user': request.user, 'error': '', 'success': ''})
        return HttpResponseNotFound

    def post(self, request):
        if request.is_ajax():
            success = ''
            error = ''
            bound_form = ProfileEdit(request.POST, instance=request.user)
            if bound_form.is_valid():
                success = '<script type="text/javascript"> location.reload() </script> '
                bound_form.save()
            else:
                error = '<div class="alert alert-danger">Произошла ошибка в обработке формы!</div>'
            return render(request, 'RExamAccounts/ProfileView.html',
                          context={'form': bound_form, 'user': request.user, 'success': success, 'error': error})
        else:
            return HttpResponseNotFound
