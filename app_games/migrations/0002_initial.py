# Generated by Django 4.1.3 on 2023-04-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_perfiles', '0001_initial'),
        ('app_games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_perfiles.userprofile'),
        ),
    ]
