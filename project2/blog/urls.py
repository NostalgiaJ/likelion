# from django.contrib import admin 생각해 보니까 blog 에 admin 이 필요 없음
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', detail, name="detail"),
    path('new/', new, name='new'),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]
