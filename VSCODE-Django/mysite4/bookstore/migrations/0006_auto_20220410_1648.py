# Generated by Django 3.1.5 on 2022-04-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20220410_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='书名'),
        ),
    ]
