# Generated by Django 2.1.15 on 2020-11-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfp', '0002_plantslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantslist',
            name='active_status',
            field=models.BooleanField(db_column='ACTIVE_STATUS', null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='display_status',
            field=models.BooleanField(db_column='DISPLAY_STATUS', null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='geo_latitude',
            field=models.FloatField(db_column='GEO_LATITUDE', null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='geo_logitude',
            field=models.FloatField(db_column='GEO_LONGITUDE', null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='location',
            field=models.CharField(db_column='LOCATION', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='plant_code',
            field=models.CharField(db_column='PLANT_CODE', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='plant_id',
            field=models.IntegerField(db_column='PLANT_ID', null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='plant_name',
            field=models.CharField(db_column='PLANT_NAME', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantslist',
            name='state_code',
            field=models.CharField(db_column='STATE_CODE', max_length=20, null=True),
        ),
    ]
