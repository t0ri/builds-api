# Generated by Django 2.2.3 on 2019-07-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0002_auto_20190729_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='bathrooms',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='lot',
            name='bedrooms',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='lot',
            name='gallery',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='lot',
            name='lot_type',
            field=models.CharField(default='undefined', max_length=100),
        ),
        migrations.AddField(
            model_name='lot',
            name='packs',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='lot',
            name='sims',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]