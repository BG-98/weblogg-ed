# Generated by Django 2.2.3 on 2019-07-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_videos/'),
        ),
    ]
