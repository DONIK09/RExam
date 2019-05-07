from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput
from fontawesome_5 import Icon
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from RExamAccounts.models import StudyGroup, UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=Icon('envelope', 'far').as_html(),
                             widget=forms.EmailInput(attrs={'placeholder': 'Введите E-Mail'}))
    password1 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    username = forms.CharField(label=Icon('user', 'far').as_html(),
                               widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    study_group = forms.ModelChoiceField(queryset=StudyGroup.objects.all(), empty_label='Выберите группу',
                                         to_field_name='id', label=Icon('users', 'fas').as_html())
    last_name = forms.CharField(label=Icon('address-card', 'far').as_html(),
                                widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    first_name = forms.CharField(label=Icon('address-card', 'far').as_html(),
                                 widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    middle_name = forms.CharField(label=Icon('address-card', 'far').as_html(),
                                  widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfile
        fields = (
            'username', 'password1', 'password2', 'email', 'study_group', 'first_name', 'last_name', 'middle_name',
            'captcha',)


class SignInForm(forms.Form):
    username = forms.CharField(label=Icon('user', 'far').as_html(),
                               widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label=Icon('key', 'fas').as_html(),
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProfileEdit(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'middle_name')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
        }
        labels = {
            'first_name': Icon('address-card', 'far').as_html(),
            'last_name': Icon('address-card', 'far').as_html(),
            'middle_name': Icon('address-card', 'far').as_html(),
        }
