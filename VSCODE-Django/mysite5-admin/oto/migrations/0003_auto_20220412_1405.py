# Generated by Django 3.1.5 on 2022-04-12 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oto', '0002_book_publisher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
    ]
