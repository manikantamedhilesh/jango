from django.db import models

# Create your models here.




class roleslist(models.Model):
    question_text = models.CharField(max_length=200)



class PlantsList(models.Model):
    plant_id = models.IntegerField(db_column='PLANT_ID',null=True)  # Field name made lowercase.
    state_code = models.CharField(db_column='STATE_CODE', max_length=20,null=True)  # Field name made lowercase.
    plant_code = models.CharField(db_column='PLANT_CODE', max_length=200,null=True)  # Field name made lowercase.
    plant_name = models.CharField(db_column='PLANT_NAME', max_length=200,null=True)  # Field name made lowercase.
    geo_latitude = models.FloatField(db_column='GEO_LATITUDE',null=True)
    geo_logitude = models.FloatField(db_column='GEO_LONGITUDE',null=True)
    active_status = models.BooleanField(db_column='ACTIVE_STATUS',null=True)
    display_status = models.BooleanField(db_column='DISPLAY_STATUS',null=True)
    location=models.CharField(db_column='LOCATION', max_length=200,null=True)

class user_details(models.Model):
    user_id = models.BigAutoField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.BigIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=150, blank=True, null=True)  # Field name made lowercase.


class userinfo(models.Model):
    EMPLOYEE_ID = models.IntegerField()
    FIRST_NAME = models.CharField(max_length=100, blank=True, null=True)
    LAST_NAME = models.CharField(max_length=100, blank=True, null=True)
    WORK_EMAIL = models.CharField(max_length=100, blank=True, null=True)
    CREATE_DATE = models.DateTimeField(auto_now_add=True, blank=True)
    USERNAME=models.CharField(max_length=100, blank=True, null=True)
    CREATED_BY=models.CharField(max_length=100, blank=True, null=True)
    ROLE =  models.CharField(max_length=100, blank=True, null=True)
    PROJECT = models.CharField(max_length=100, blank=True, null=True)
    APP_ID = models.CharField(max_length=100, blank=True, null=True)
    IS_ACTIVE = models.BooleanField(max_length=100, blank=True, null=True)

class tokenblocklist(models.Model):
    token = models.CharField(max_length=500, null=True, blank=True)
    user = models.CharField(db_column='User',max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

class leaktest_failed_img_details(models.Model):
    date=models.CharField(db_column='Date', max_length=20,null=True)
    station = models.CharField(db_column='STATION', max_length=20,null=True)  # Field name made lowercase.
    plant_code = models.CharField(db_column='PLANT_CODE', max_length=200,null=True)  # Field name made lowercase.
    plant_name = models.CharField(db_column='PLANT_NAME', max_length=200,null=True)  # Field name made lowercase.
    line = models.CharField(db_column='LINE',max_length=200,null=True)
    img_url = models.CharField(db_column='IMG_URL',max_length=200,null=True)
    leak_test_type = models.CharField(db_column='LEAK_TEST_TYPE',max_length=20,null=True)
    uploaded_by = models.CharField(db_column='UPLOADED_BY',max_length=200,null=True)
    is_active = models.BooleanField(db_column='IS_ACTIVE',null=True,default=True)
    worker_at_line=models.CharField(db_column='PERSON_AT_LINE', max_length=200,null=True)
    updated_by=models.CharField(db_column='UPDATED_BY', max_length=200,null=True)

class backtracking(models.Model):
    plant_name = models.CharField(db_column='PLANT_NAME', max_length=200,null=True)
    plant_code = models.CharField(db_column='PLANT_CODE', max_length=200,null=True)
    line = models.CharField(db_column='LINE',max_length=200,null=True)
    leak_test_img_url = models.CharField(db_column='IMG_URL',max_length=200,null=True)
    leak_test_type = models.CharField(db_column='LEAK_TEST_TYPE',max_length=20,null=True)
    upload_time = models.DateTimeField(db_column='UPLOAD_TIME',blank=True)
    matched_c4_fp_img_url = models.CharField(db_column='MATCHED_C4_FP_IMG_URL',max_length=200,null=True)
    matched_c4_fp_time = models.DateTimeField(db_column='MATCHED_C4_FP_TIME',blank=True)
    matched_c3_fp_img_url = models.CharField(db_column='MATCHED_C3_FP_IMG_URL',max_length=200,null=True)
    matched_c3_fp_time = models.DateTimeField(db_column='MATCHED_C3_FP_TIME',blank=True)
    matched_c2_fp_img_url = models.CharField(db_column='MATCHED_C2_FP_IMG_URL',max_length=200,null=True)
    matched_c2_fp_time = models.DateTimeField(db_column='MATCHED_C2_FP_TIME',blank=True)
    matched_c1_left_fp_img_url = models.CharField(db_column='MATCHED_C1_LEFT_FP_IMG_URL',max_length=200,null=True)
    matched_c1_left_fp_time = models.DateTimeField(db_column='MATCHED_C1_LEFT_FP_TIME',blank=True)
    matched_c1_right_fp_img_url = models.CharField(db_column='MATCHED_C1_RIGHT_FP_IMG_URL',max_length=200,null=True)
    matched_c1_right_fp_time = models.DateTimeField(db_column='MATCHED_C1_RIGHT_FP_TIME',blank=True)
    is_active = models.BooleanField(db_column='IS_ACTIVE',null=True,default=True)



