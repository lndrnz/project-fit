# Generated by Django 4.0.3 on 2023-04-25 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyms_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='title',
            new_name='name',
        ),
    ]
