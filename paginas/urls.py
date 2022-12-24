from django.urls import path
from .views import LayoutView#, TableView
from django.contrib import admin
from paginas import views  
from django.urls import include, re_path

urlpatterns = [
    path('', views.search, name='tables'),
    path('edit/<int:id>', views.editemp),
    path('update/<int:id>', views.updateemp),
    re_path(r'^search/$', views.search, name='tables'),
    path('layout', LayoutView.as_view(), name='layout')
]