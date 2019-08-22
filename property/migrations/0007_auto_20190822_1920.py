# Generated by Django 2.2.4 on 2019-08-22 16:20

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализированный номер владельца'),
        ),
    ]
