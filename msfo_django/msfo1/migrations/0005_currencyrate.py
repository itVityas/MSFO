# Generated by Django 5.0.3 on 2024-12-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msfo1', '0004_reportfile_debt_report_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
            options={
                'unique_together': {('currency', 'date')},
            },
        ),
    ]
