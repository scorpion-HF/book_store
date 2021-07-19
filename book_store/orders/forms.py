from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('address', 'postal_code', 'phone_number')
        labels = {
            'address': 'آدرس: ',
            'postal_code': 'کد پستی: ',
            'phone_number': 'شماره تلفن: ',
        }
        help_texts = {
            'address': 'آدرس خود را دقیق وارد نمایید:',
            'postal_code': 'کد پستی خود را بدون خط تیره و پیوسته وارد نمایید: ',
            'phone_number': 'جهت سهولت ارتباط لطفا شماره تلفن همراه خود را به صورت کامل وارد نمایید: '
        }
