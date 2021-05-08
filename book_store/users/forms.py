from django.forms import ModelForm, TextInput, Textarea
from .models import User


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
