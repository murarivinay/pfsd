# Generated by Django 5.0 on 2024-02-06 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='password',
            new_name='feedback',
        ),
    ]