# Generated by Django 3.1.7 on 2021-06-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210507_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن همراه'),
        ),
    ]
