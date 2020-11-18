"""Digital_Fingerprinting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import sys,os
from django.urls import path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  dfp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addplant/', views.insert_plant),
    path('adduser/', views.adduser),
    path('login/', views.login),
    path('plantlist/', views.plant_list),
    path('uploadfailedimg/',views.upload_failed_img),
    path('failedimgdetails',views.get_failed_img_details),
    path('adduserinfo/', views.adduserinfo),
    path('logout/', views.logout),
    path('backtrack_images/', views.backtrack_images),
    path('kpi/', views.kpi),
    

]
