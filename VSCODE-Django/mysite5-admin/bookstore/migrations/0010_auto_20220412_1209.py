# Generated by Django 3.1.5 on 2022-04-12 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_book_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]
