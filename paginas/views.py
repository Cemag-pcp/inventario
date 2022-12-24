from django.views.generic import TemplateView
from .models import tb_balanco
from django.shortcuts import render
from paginas.models import tb_balanco
from paginas.forms import empforms
from django.contrib import messages
from .filters import UserFilter
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#class TableView(TemplateView):
#    template_name = 'tables1.html'

def displaydata(request):
    results=tb_balanco.objects.all()
    return render(request,"tables.html", {'tb_balanco':results})

def editemp(request,id):
    displayemp=tb_balanco.objects.get(id=id)
    return render(request, "edit.html", {"tb_balanco":displayemp})

def updateemp(request,id):
    updateemp=tb_balanco.objects.get(id=id)
    form=empforms(request.POST,instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return render(request, "edit.html", {"tb_balanco":updateemp})

def search(request):
    user_list = tb_balanco.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'tables.html', {'filter': user_filter})