from django.contrib import admin
from django.urls import path

from patsumapp import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('starter/', views.starter, name='starter'),
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('service/', views.service, name='service'),
]
