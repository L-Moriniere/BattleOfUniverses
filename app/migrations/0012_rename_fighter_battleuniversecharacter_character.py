# Generated by Django 4.0 on 2022-01-27 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_battleuniverse_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battleuniversecharacter',
            old_name='fighter',
            new_name='character',
        ),
    ]
