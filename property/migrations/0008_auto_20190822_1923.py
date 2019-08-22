# Generated by Django 2.2.4 on 2019-08-22 16:23

from django.db import migrations
import phonenumbers


def format_phone_number(phone_number):
    try:
        parse_phone_number = phonenumbers.parse(phone_number, 'RU')
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

    return phonenumbers.format_number(
        parse_phone_number,
        phonenumbers.PhoneNumberFormat.INTERNATIONAL
    ) if phonenumbers.is_valid_number(parse_phone_number) else None


def transfer_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        raw_phone_number = flat.owners_phonenumber
        pure_phone_number = format_phone_number(raw_phone_number)
        if pure_phone_number is None:
            continue
        flat.owner_phone_pure = pure_phone_number
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_phone_pure = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20190822_1920'),
    ]

    operations = [
        migrations.RunPython(transfer_phone_numbers, move_backward),
    ]
