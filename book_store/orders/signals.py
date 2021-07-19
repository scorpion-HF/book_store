from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from jalali_date import datetime2jalali


@receiver(post_save, sender=Order)
def create_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'سفارشات | اقیانوس دانش',
            'یک سفارش در تاریخ {} انجام شده است. جهت مشاهده به پنل ادمین بخش سفارشات مراجعه فرمایید'.
            format(datetime2jalali(instance.date).strftime('%H:%M:%S _ %y/%m/%d')),
            None,
            ['saeedalbooyeh@gmail.com'],
            fail_silently=False,
        )


