# Generated by Django 5.0.3 on 2024-09-24 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msfo8', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrance',
            name='id_file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='msfo8.files'),
            preserve_default=False,
        ),
    ]
