# Generated by Django 2.2.3 on 2019-07-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190724_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_pics/'),
        ),
    ]
