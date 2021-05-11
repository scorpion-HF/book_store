from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse_lazy

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
