# Generated by Django 4.0.3 on 2023-05-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
