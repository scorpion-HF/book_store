# Generated by Django 3.1.7 on 2021-04-28 13:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20210428_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[300, 300], upload_to='books_images/'),
        ),
    ]
