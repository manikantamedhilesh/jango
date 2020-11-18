# Generated by Django 2.1.15 on 2020-11-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfp', '0003_auto_20201111_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('user_id', models.BigAutoField(db_column='USER_ID', primary_key=True, serialize=False)),
                ('employee_id', models.BigIntegerField(db_column='EMPLOYEE_ID')),
                ('username', models.CharField(db_column='USERNAME', max_length=50, unique=True)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=150, null=True)),
            ],
        ),
    ]
