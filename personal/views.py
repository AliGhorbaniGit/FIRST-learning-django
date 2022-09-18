from django.shortcuts import render
from .models import ViewPersonal


def person_show(request, pk):
    data = ViewPersonal.objects.get(pk=pk)
    return render(request,'personal/personal.html',{'data':data})
