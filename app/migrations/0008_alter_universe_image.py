# Generated by Django 4.0 on 2022-01-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_battleroyale_battleuniverse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universe',
            name='image',
            field=models.ImageField(null=True, upload_to='Universe'),
        ),
    ]
