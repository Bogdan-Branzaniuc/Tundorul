# Generated by Django 3.2.18 on 2023-04-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tundorul', '0012_auto_20230424_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamschedule',
            name='timezone',
            field=models.CharField(default='Europe/Bucharest', max_length=200),
        ),
    ]