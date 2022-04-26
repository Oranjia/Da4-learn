# Generated by Django 3.1.5 on 2022-04-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oto', '0003_auto_20220412_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=11, verbose_name='书名')),
                ('authors', models.ManyToManyField(to='oto.Author')),
            ],
        ),
    ]
