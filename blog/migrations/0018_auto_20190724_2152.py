# Generated by Django 2.2.3 on 2019-07-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190724_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_pics/'),
        ),
    ]
