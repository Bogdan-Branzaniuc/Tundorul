# Generated by Django 3.2.18 on 2023-05-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tundorul', '0015_auto_20230508_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='subscribed_since',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='channel_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
