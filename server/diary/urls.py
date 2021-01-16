from django.contrib import admin
from django.urls import path

from diary.views import article_list, article_read


app_name = 'diary'

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<int:pk>/', article_read, name='article_read'),
]
