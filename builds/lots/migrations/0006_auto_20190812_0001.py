# Generated by Django 2.2.3 on 2019-08-12 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0005_auto_20190811_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='packs',
        ),
        migrations.AddField(
            model_name='lot',
            name='images',
            field=models.TextField(default='undefined'),
        ),
    ]
