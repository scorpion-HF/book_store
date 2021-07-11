from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse_lazy
from django import forms
from .models import User
from allauth.account.forms import SignupForm, LoginForm, set_form_field_order, PasswordField
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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'آدرس ایمیل'
        self.fields['password1'].label = 'کلمه عبور'
        self.fields['password2'].label = 'تکرار کلمه عبور'
        self.fields['email'].widget.attrs = {
            'placeholder': 'ایمیل',
        }
        self.fields['password1'].widget.attrs = {
            'placeholder': 'کلمه عبور',
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': 'تکرار کلمه عبور',
        }


class AllauthLoginForm(LoginForm):
    password = PasswordField(label="کلمه عبور", autocomplete="current-password")
    remember = forms.BooleanField(label="مرا به خاطر بسپار", required=False)
    captcha = CaptchaField(label='حاصل عبارت را وارد نمایید:')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'آدرس ایمیل'
        self.fields['login'].widget.attrs = {
            'placeholder': 'ایمیل',
        }
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # this line sets your form's method to post
        self.helper.form_action = reverse_lazy('account_login')  # this line sets the form action
        self.helper.layout = Layout(
            'login',
            'password',
            'remember',
            'captcha',
            Submit('submit', u'Submit', css_class='btn btn-success'),
        )
