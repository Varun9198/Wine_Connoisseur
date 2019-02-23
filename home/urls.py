from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('home/filter/', filter, name='filter'),
    path('home/sort_data/', sorted_data, name='sort')
]
