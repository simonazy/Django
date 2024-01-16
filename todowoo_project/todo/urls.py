from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('<int:todo_pk>/complete', views.completetodo, name='completedtodos'),
    path('<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]