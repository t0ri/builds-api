# Generated by Django 2.2.3 on 2019-08-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0004_auto_20190731_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='title',
            new_name='name',
        ),
    ]
