# Generated by Django 5.0.3 on 2024-12-09 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_1c', models.CharField(max_length=50)),
                ('sorting_number', models.IntegerField()),
                ('db_account_number', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('account_1c', 'sorting_number')},
            },
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_byn', models.DecimalField(decimal_places=2, max_digits=15)),
                ('debt_contract_currency', models.DecimalField(decimal_places=2, max_digits=15)),
                ('contract_currency', models.CharField(max_length=10)),
                ('date_of_debt', models.DateField()),
                ('payment_term_days', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msfo1.accountmapping')),
                ('counterparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msfo1.counterparty')),
            ],
        ),
    ]
