# Generated by Django 3.2 on 2022-04-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_description',
            field=models.TextField(default='Yummy meal description goes here', max_length=1000),
        ),
    ]
