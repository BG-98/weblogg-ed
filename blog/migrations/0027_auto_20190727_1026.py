# Generated by Django 2.2.3 on 2019-07-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20190727_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
    ]
