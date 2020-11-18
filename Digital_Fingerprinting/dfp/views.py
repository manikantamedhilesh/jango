from django.shortcuts import render
from .authentication import validation

from .models import PlantsList, user_details,userinfo,tokenblocklist,leaktest_failed_img_details,backtracking

import jwt, json,os,sys
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import get_authorization_header
import ast
import base64
from rest_framework_jwt.settings import api_settings
import datetime as dt

from azure.storage.blob import BlockBlobService, PublicAccess,ContentSettings
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime, timedelta
from calendar import timegm

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


#TO add plants in the database. (incomplete)
@csrf_exempt

def insert_plant(request):
    if request.method == 'GET':

        print('respose_data:', request)

        return JsonResponse({'message':'success'})


#dummy login service

@csrf_exempt
def login(request):
    login_auth = get_authorization_header(request).split()
    if request.method == 'POST':
        try:
        
            print('login_auth[0]',login_auth[0])

            if login_auth[0].decode('utf-8').lower().strip() =='token':
                login_token = login_auth[1]
                credentials_decode = base64.b64decode(login_token)
                credentials_decode = credentials_decode.decode('utf-8')
                username = credentials_decode.split(':')[0]
                password = credentials_decode.split(':')[1]
                password = password.encode("utf-8")
                password = base64.b64encode(password)

                try:
                    user_data=list(user_details.objects.filter(username=username, password=password).values())
                    print(".........user_data.......",user_data)
                    if len(user_data)==0:
                        return JsonResponse({'message': 'Invalid Credentials or Unauthorized User', 'success': 0})
                    else:
                        
                        payload = {'username': username,'exp': dt.datetime.utcnow() + dt.timedelta(hours=3)}
                        token = jwt.encode(payload, "SECRET_KEY").decode('utf-8')
                        print('TOKEN::\n',token)

                        
                        user_info=list(userinfo.objects.filter(USERNAME=username,IS_ACTIVE=True).values())

                        # username = user_info[0]['USERNAME']
                        emp_id = user_info[0]['EMPLOYEE_ID']
                        firstname = user_info[0]['FIRST_NAME']
                        lastname = user_info[0]['LAST_NAME']
                        user_role = user_info[0]['ROLE']

                        data={'username':username,'token':token,'emp_id':emp_id,'firstname':firstname,'lastname':lastname,'user_role':user_role}
                        print('data:::',data)
                        return JsonResponse({'data':data,'message': 'Login Successful', 'success': 1}, status=200, content_type="application/json")

                   
                except Exception as e:
                    msg = 'Invalid Credentials or Unauthorized User'
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print(type(e))  # the exception instance
                    print(e.args)  # arguments stored in .args
                    print(e)
                    return JsonResponse({'message': msg, 'success': 0})

        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            return JsonResponse({'message': msg,'success':2})
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})    


#adduser API is to add dummy users in the SQL database

@csrf_exempt
def adduser(request):

    if request.method == 'POST':
        
        users = ['Director operations','Plant Manager']
        count =1
        for user in range(len(users)):
            user_id = user
            employee_id = count
            username = users[user]
            password = 'password'
            password = password.encode("utf-8")
            password = base64.b64encode(password)
            print('password::\t',password)

            user_data = user_details(user_id=user_id, employee_id=employee_id,username = username, password=password)
            user_data.save()
        return JsonResponse({'message': 'user data inserted', 'success': 1})

    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})



#plant_list API will return list of the plants.
@csrf_exempt
def plant_list(request):
    if request.method == 'GET':
        response = validation(request)
        try:
            try:
                response_data = response.content
                response_data = response_data.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
            response_dict = ast.literal_eval(response_data)
            
            if 'username' in response_dict.keys():
                user_name = response_dict['username']
                projects_data=[]
                data = PlantsList.objects.filter().all()
                for proj in data:
                    print('proj::\t',proj)
                    projects_data.append({'plant': proj.plant_name})
                projest_d = {"data": projects_data, 'success': 1}
                return JsonResponse(projest_d)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})


@csrf_exempt
def adduserinfo(request):

    if request.method == 'POST':
        
        # users = ['Director operations','Plant Manager']
        # count =1
        
        EMPLOYEE_ID = 2
        FIRST_NAME = 'Plant'
        LAST_NAME = 'Manager'
        WORK_EMAIL = ''
        USERNAME='Plant manager'
        CREATED_BY='Admin'
        ROLE =  'plant manager'
        PROJECT = 'dfp'
        APP_ID = '1'
        IS_ACTIVE = True

        user_data = userinfo(EMPLOYEE_ID = EMPLOYEE_ID,FIRST_NAME = FIRST_NAME, LAST_NAME = LAST_NAME,
                    USERNAME=USERNAME,CREATED_BY=CREATED_BY,ROLE =  ROLE, PROJECT = PROJECT, APP_ID = APP_ID,
                    IS_ACTIVE = True)
        user_data.save()

        # user_details.objects.filter(username='Director operations').update(user_id=1)
        # user_details.objects.filter(username='Plant Manager').update(employee_id=2,user_id=2)

        return JsonResponse({'message': 'user data inserted', 'success': 1})

    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})


@csrf_exempt
def logout(request):
    if request.method == 'GET':
        response = validation(request)
        try:
            try:
                response_data = response.content.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})

            response_dict = ast.literal_eval(response_data)
            print('responce dict logout::', response_data)
            if 'username' in response_dict.keys():
                login_auth = get_authorization_header(request).split()
                token = login_auth[1].decode('utf-8')
                print('token::', token)
                token_save = tokenblocklist(token=token, user=response_dict['username'])
                token_save.save()
                return JsonResponse({'message': "Logout Successful", 'success': 1})

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})

        


#For uploading leak test failed images 

@csrf_exempt
def upload_failed_img(request):
    if request.method == 'POST':
        
        response = validation(request)
        try:
            try:
                response_data = response.content.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
            if request.FILES['file']:
                # blob_service_client = BlockBlobService(
                #     account_name='rslennox8087050449', account_key='9g/6lQB8aBil4o981PRo7U7uv9Zq/wezwkAaQGjSxCS9SCdJX6m0OvJBZ9DCKTHVfZEvvBxrLml/spFQyjkH9g==')
                connect_str='DefaultEndpointsProtocol=https;AccountName=rslennox8087050449;AccountKey=9g/6lQB8aBil4o981PRo7U7uv9Zq/wezwkAaQGjSxCS9SCdJX6m0OvJBZ9DCKTHVfZEvvBxrLml/spFQyjkH9g==;EndpointSuffix=core.windows.net'
                blob_service_client = BlobServiceClient.from_connection_string(connect_str)

                # Create a container called 'quickstartblobs'.
                container_name = 'lennox-data'

                myfiles = request.FILES.getlist('file')
                date = request.POST.get('date')
                station = request.POST.get('station')
                line = request.POST.get('line')
                # plant_code = request.POST.get('plant_code')
                plant_name = request.POST.get('plant_name')
                person_at_line=request.POST.get('person_at_line')


                for fle in myfiles:
                    file_name = fle.name
                    
                    print('file name::', file_name)
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

                    blob_client.upload_blob(fle)
                    img_url='https://rslennox8087050449.blob.core.windows.net/lennox-data/' + file_name
                    print('\t', 'https://rslennox8087050449.blob.core.windows.net/lennox-data/' + file_name)
                    leaktest_failed_img_details(plant_name=plant_name,date=date,img_url=img_url,station=station,line=line,worker_at_line=person_at_line).save()

            return JsonResponse({"message":"success"})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})

# Failed slab image urls filtred by plant

@csrf_exempt
def get_failed_img_details(request):
    if request.method == 'POST':
        
        response = validation(request)
        try:
            try:
                response_data = response.content.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
            
            if  json.loads(request.body):

                data = json.loads(request.body)

                plant_name=data['plant_name']
                
                data = list(leaktest_failed_img_details.objects.filter(plant_name=plant_name).values())
                print(data)
                    # leaktest_failed_img_details(plant_name=plant_name,date=date,img_url=img_url,station=station,line=line,worker_at_line=person_at_line).save()

            return JsonResponse({"data":data, 'message':'success'})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})


@csrf_exempt
def backtrack_images(request):
    if request.method == 'POST':
        
        response = validation(request)
        try:
            try:
                response_data = response.content.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
            if  json.loads(request.body):

                data = json.loads(request.body)

                leak_test_img_url=data['img_url']
                plant_name=data['plant_name']

                backtrack_data = list(backtracking.objects.filter(plant_name=plant_name,leak_test_img_url=leak_test_img_url).values())
                img_urls = []

                for obj in backtrack_data:
                    img_urls.append({'leak_test_img_url': obj['leak_test_img_url'],'matched_c4_fp_img_url':obj['leak_test_img_url'],
                    'matched_c3_fp_img_url': obj['matched_c3_fp_img_url'],'matched_c2_fp_img_url':obj['matched_c2_fp_img_url'],
                    'matched_c1_left_fp_img_url': obj['matched_c1_left_fp_img_url'],
                    'matched_c1_right_fp_img_url':obj['matched_c1_right_fp_img_url']})

                return JsonResponse({'data':img_urls,'message':'data sucessfully retrieved', 'sucess':1})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})


@csrf_exempt

def kpi(request):
    if request.method == 'POST':
        
        response = validation(request)
        try:
            try:
                response_data = response.content.decode('utf-8')
            except:
                return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
            if  json.loads(request.body):

                data = json.loads(request.body)

                plant_name=data['plant_name']
                leak_test_count = backtracking.objects.filter(plant_name=plant_name).values().count()
                water_leak_test_count = backtracking.objects.filter(plant_name=plant_name,leak_test_type='water').values().count()
                helium_leak_test_count = backtracking.objects.filter(plant_name=plant_name,leak_test_type='helium').values().count()
                
                autobrazer_count = 200
                coil_build_station_count= 150
                manifold_or_adding_fittings_count = 100

                kpi_count = {'leak_test':leak_test_count,'water_leak_test':water_leak_test_count,
                            'helium_leak_test':helium_leak_test_count,'autobrazer':autobrazer_count,
                            'coil_build_station':coil_build_station_count,'manifold_or_adding_fittings':manifold_or_adding_fittings_count
                                }
               
                return JsonResponse({'data':kpi_count,'message':'data sucessfully retrieved', 'sucess':1})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN", 'success': 2})
        return response
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})



