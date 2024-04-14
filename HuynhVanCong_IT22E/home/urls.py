from django.urls import path
from .import views

#Insert your link urls here
urlpatterns = [
    path('', views.index )     
 ]
 