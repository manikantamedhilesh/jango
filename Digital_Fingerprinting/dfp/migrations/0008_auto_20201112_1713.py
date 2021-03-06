# Generated by Django 2.1.15 on 2020-11-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfp', '0007_auto_20201112_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backtracking',
            name='matched_c1_left_fp_time',
            field=models.DateTimeField(blank=True, db_column='MATCHED_C1_LEFT_FP_TIME'),
        ),
        migrations.AlterField(
            model_name='backtracking',
            name='matched_c2_fp_time',
            field=models.DateTimeField(blank=True, db_column='MATCHED_C2_FP_TIME'),
        ),
        migrations.AlterField(
            model_name='backtracking',
            name='matched_c3_fp_time',
            field=models.DateTimeField(blank=True, db_column='MATCHED_C3_FP_TIME'),
        ),
        migrations.AlterField(
            model_name='backtracking',
            name='matched_c4_fp_time',
            field=models.DateTimeField(blank=True, db_column='MATCHED_C4_FP_TIME'),
        ),
        migrations.AlterField(
            model_name='backtracking',
            name='matched_c4_right_fp_time',
            field=models.DateTimeField(blank=True, db_column='MATCHED_C1_RIGHT_FP_TIME'),
        ),
        migrations.AlterField(
            model_name='backtracking',
            name='upload_time',
            field=models.DateTimeField(blank=True, db_column='UPLOAD_TIME'),
        ),
    ]
