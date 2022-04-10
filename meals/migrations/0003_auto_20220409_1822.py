# Generated by Django 3.2 on 2022-04-09 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meals', '0002_meal_meal_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['-in_stock']},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-planned']},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_name',
            field=models.CharField(max_length=200),
        ),
    ]