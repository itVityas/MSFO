# Generated by Django 5.0.3 on 2024-12-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msfo1', '0005_currencyrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyrate',
            name='rate',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
