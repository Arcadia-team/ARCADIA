# Generated by Django 4.1.3 on 2023-04-24 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_games', '0003_game_partidas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='partidas',
            new_name='NumeroPartidas',
        ),
    ]