# Generated by Django 3.0.4 on 2021-09-27 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200606_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverifyrecord',
            name='add_time',
        ),
    ]
