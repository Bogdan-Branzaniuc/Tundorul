# Generated by Django 3.2.18 on 2023-05-08 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tundorul', '0016_auto_20230508_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='following_since',
        ),
    ]
