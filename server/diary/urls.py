from django.contrib import admin
from django.urls import path

from diary.views import article_list


app_name = 'diary'

urlpatterns = [
    path('', article_list, name='article_list'),
]
