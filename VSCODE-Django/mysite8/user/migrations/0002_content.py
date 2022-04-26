# Generated by Django 3.1.5 on 2022-04-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=11, verbose_name='文章名字')),
                ('picture', models.FileField(upload_to='picture')),
            ],
        ),
    ]
