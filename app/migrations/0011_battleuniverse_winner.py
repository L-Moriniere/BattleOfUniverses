# Generated by Django 4.0 on 2022-01-27 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_battleuniverse_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleuniverse',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.character'),
        ),
    ]
