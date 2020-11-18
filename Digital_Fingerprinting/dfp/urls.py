from . import views

from django.urls import path

urlpatterns = [
    path('addplant/', views.insert_plant),
    path('adduser/', views.adduser),
    path('login/', views.login)

]