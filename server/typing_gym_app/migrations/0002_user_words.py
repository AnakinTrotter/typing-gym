# Generated by Django 3.2.10 on 2022-02-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typing_gym_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='words',
            field=models.JSONField(default={'test': 0}),
        ),
    ]
