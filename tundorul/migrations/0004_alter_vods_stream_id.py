# Generated by Django 3.2.18 on 2023-05-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tundorul', '0003_userprofile_profile_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vods',
            name='stream_id',
            field=models.CharField(default=0, max_length=255, unique=True),
        ),
    ]