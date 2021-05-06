from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'postal_code', )
        labels = {
            'address': 'آدرس: ',
            'postal_code': 'کد پستی: ',
        }
        help_texts = {
            'address': 'آدرس خود را دقیق وارد نمایید:',
            'postal_code': 'کد پستی خود را بدون خط تیره و پیوسته وارد نمایید : ',
        }
