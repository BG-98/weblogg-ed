# Generated by Django 2.2.3 on 2019-07-27 09:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0027_auto_20190727_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rating_count',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
