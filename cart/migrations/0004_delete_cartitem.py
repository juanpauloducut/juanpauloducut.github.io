# Generated by Django 5.0.2 on 2024-04-25 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
