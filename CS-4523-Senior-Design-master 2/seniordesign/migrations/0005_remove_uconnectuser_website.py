# Generated by Django 2.1.2 on 2018-12-11 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seniordesign', '0004_uconnectuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uconnectuser',
            name='website',
        ),
    ]
