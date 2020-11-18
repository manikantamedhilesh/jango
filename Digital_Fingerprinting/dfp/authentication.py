import jwt,sys,os
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import get_authorization_header
from .models import PlantsList, user_details,userinfo,tokenblocklist
import datetime as dt
from datetime import datetime, timedelta
from calendar import timegm



def validation(request):
    auth = get_authorization_header(request).split()

    if len(auth)==0:
        return JsonResponse({'message': "Internal server error",'success':2} )
    if len(auth) == 1:
        msg = 'Invalid token header '
        return JsonResponse({'message': msg,'success':2})
    elif len(auth) > 2:
        msg = 'Invalid token header'
        return JsonResponse({'message': msg,'success':2})
    try:
        print('auth[0]',auth[0])
        if auth[0].decode('utf-8').lower().strip() =='token':
            token = auth[1]
            print('token in def:', token)
            if token == "null":
                msg = 'Null token not allowed'
                return JsonResponse({'message': msg, 'success': 2})
            return authenticate_credentials(token)

    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        return JsonResponse({'message': msg,'success':2})

def authenticate_credentials(token):
    # model = get_model()
    # token = bytes(token)
    # print('came to authenticate token def::', token)
    try:

        try:
            # payload=jwt
            payload = jwt.decode(token, "SECRET_KEY", )
        except jwt.InvalidSignatureError:
            return JsonResponse({'message': "INVALID_TOKEN",'success':2})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': "Session Expired ,Please login",'success':2})
        except jwt.DecodeError:
            return JsonResponse({'message': "INVALID_TOKEN",'success':2})

        username = payload['username']
        print('username:::\t',username)
        # email = payload['email']
        time = payload['exp']
        print('time::', type(time))
        # msg = {'Error': "Token mismatch", 'status': "401"}
        try:
            # print(userinfo.objects.get(FIRST_NAME=email, WORK_EMAIL=userid))

            if tokenblocklist.objects.filter(token=token).count() > 0 :
                return JsonResponse({'message': "Session Expired ,Please login", 'success': 2})
            else:
                
                user = userinfo.objects.filter(USERNAME=username,IS_ACTIVE=True).all()
                for obj in user:
                    print('obj.USERNAME::;\t',obj.USERNAME)
                    username_db = obj.USERNAME
                    
                    # email_db = obj.WORK_EMAIL
                    print('token in auth::',token)
                    if username_db.lower() == username.lower():
                        if time:
                            refresh_limit = dt.timedelta(days=1)
                            if isinstance(refresh_limit, timedelta):
                                # refresh_limit = refresh_limit.seconds
                                refresh_limit = (refresh_limit.days * 24 * 3600 + refresh_limit.seconds)
                            expiration_timestamp = time + int(refresh_limit)
                            now_timestamp = timegm(datetime.utcnow().utctimetuple())
                            if now_timestamp > expiration_timestamp:
                                msg = 'Refresh has expired.'
                                # raise serializers.ValidationError(msg)
                                return JsonResponse({"msg": msg})
                            new_payload = {'username': username, 'exp': expiration_timestamp}
                            new_token = jwt.encode(new_payload, key='SECRET_KEY')
                            print('token in if condtions:', new_token)

                            return JsonResponse({'token': token.decode('utf-8'), 'username': username})
            if not username:
                return JsonResponse({'message': "INVALID_TOKEN",'success':2})

        except userinfo.DoesNotExist:
            return JsonResponse({'message': "Internal server error",'success':2})
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)
        return JsonResponse({'message':'Error in create_user insertion', 'success': 0})

    except jwt.ExpiredSignatureError:
        return JsonResponse({'message': "Session Expired ,Please login",'success':2} )



