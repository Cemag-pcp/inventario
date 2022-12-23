from django.urls import path
#from .views import TablesView
from django.contrib import admin
from paginas import views  
from django.urls import include, re_path

urlpatterns = [
    #path('', TablesView.as_view(), name='tables'),
    path('', views.search, name='tables'),
    path('edit/<int:id>', views.editemp),
    path('update/<int:id>', views.updateemp),
    re_path(r'^search/$', views.search, name='tables'),
]

