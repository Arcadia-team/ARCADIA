# Generated by Django 4.1.3 on 2023-04-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_games', '0009_remove_game_numeropartidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='numeroPartidas',
            field=models.IntegerField(default=0),
        ),
    ]
