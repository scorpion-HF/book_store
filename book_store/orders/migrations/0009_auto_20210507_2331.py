# Generated by Django 3.1.7 on 2021-05-07 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0027_auto_20210507_2244'),
        ('orders', '0008_auto_20210505_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'قلم سبد خرید', 'verbose_name_plural': 'اقلام سبد خرید'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'قلم سفارش', 'verbose_name_plural': 'اقلام سفارش'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart', verbose_name='سبد خرید'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='عنوان قلم سبد خرید'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(verbose_name='آدرس ارسال'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_posted',
            field=models.BooleanField(default=False, verbose_name='ارسال شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=0, max_length=10, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_quantity',
            field=models.IntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_title',
            field=models.CharField(max_length=100, verbose_name='عنوان قلم سفارش'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='سفارش'),
        ),
    ]
