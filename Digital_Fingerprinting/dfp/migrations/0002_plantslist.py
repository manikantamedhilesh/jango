# Generated by Django 2.1.15 on 2020-11-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_id', models.IntegerField(db_column='PLANT_ID')),
                ('state_code', models.CharField(db_column='STATE_CODE', max_length=20)),
                ('plant_code', models.CharField(db_column='PLANT_CODE', max_length=200)),
                ('plant_name', models.CharField(db_column='PLANT_NAME', max_length=200)),
                ('geo_latitude', models.FloatField(db_column='GEO_LATITUDE')),
                ('geo_logitude', models.FloatField(db_column='GEO_LONGITUDE')),
                ('active_status', models.BooleanField(db_column='ACTIVE_STATUS')),
                ('display_status', models.BooleanField(db_column='DISPLAY_STATUS')),
                ('location', models.CharField(db_column='LOCATION', max_length=200)),
            ],
        ),
    ]
