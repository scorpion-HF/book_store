from django.forms import ModelForm, TextInput, Textarea
from .models import User
from allauth.account.forms import SignupForm, LoginForm
from captcha.fields import CaptchaField


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'postal_code')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control here'}),
            'last_name': TextInput(attrs={'class': 'form-control here'}),
            'phone_number': TextInput(attrs={'class': 'form-control here'}),
            'postal_code': TextInput(attrs={'class': 'form-control here'}),
            'address': Textarea(attrs={'class': 'form-control'}),
        }


class AllauthSignupForm(SignupForm):
    captcha = CaptchaField(label='حاصل عبارت را وارد نمایید:')
    field_order = ('email', 'password1', 'password2', 'captcha')


class AllauthLoginForm(LoginForm):
    captcha = CaptchaField(label='حاصل عبارت را وارد نمایید:')
