# Generated by Django 3.1.5 on 2022-04-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_book_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
    ]
