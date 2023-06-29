from django.contrib import admin
from django.urls import path
from . import views
# print("we are in urls")
urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('buy1/', views.buy, name='buy'),
    path('buy2/', views.buy, name='buy'),
    path('buy3/', views.buy, name='buy'),
    path('buy4/', views.buy, name='buy'),
    path('buy5/', views.buy, name='buy'),
    path('buy6/', views.buy, name='buy'),
    path('buy7/', views.buy, name='buy'),
    path('buy8/', views.buy, name='buy'),
    path('buy9/', views.buy, name='buy'),
  #  path('subcontact/', views.subcontact, name='subcontact')

]