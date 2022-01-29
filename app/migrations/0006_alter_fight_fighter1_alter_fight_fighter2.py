# Generated by Django 4.0 on 2022-01-22 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_fight_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='fighter1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fighter1', to='app.character'),
        ),
        migrations.AlterField(
            model_name='fight',
            name='fighter2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fighter2', to='app.character'),
        ),
    ]
