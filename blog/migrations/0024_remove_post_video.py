# Generated by Django 2.2.3 on 2019-07-26 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190726_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
