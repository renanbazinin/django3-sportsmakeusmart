
from django.contrib import admin
from django.urls import path,include
from main import views


urlpatterns = [
    


    #path('signin/', views.signin, name = 'signin'),
    
    #path('signin/home', views.main, name = 'main'),
    path('', views.signin, name= 'signin'),
    path('home/', views.main, name= 'main'),
    #path('sendscore/', views.sendscore, name= 'sendscore'),

]
