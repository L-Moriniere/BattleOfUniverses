# Generated by Django 4.0 on 2022-01-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_fight_battleuniverse'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleuniverse',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]