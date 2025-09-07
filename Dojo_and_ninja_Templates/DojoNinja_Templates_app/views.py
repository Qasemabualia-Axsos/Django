from django.shortcuts import render ,redirect
from .models import Dojo,Ninja
# Create your views here.

def index(request):
    data={
        "Dojo":Dojo.objects.all(),
        "Ninja":Ninja.objects.all()
    }
    return render (request,'index.html',data)

def add_dojo(request):
    data={
        "Dojos":Dojo.objects.all()
    }
    if request.method=='POST':
        name=request.POST.get('name')
        city=request.POST.get('city')
        state=request.POST.get('state')

        Dojo.objects.create(name=name,city=city,state=state)
        return redirect('/')
    return redirect('/')


def add_ninja(request):
    data={
        "Dojo":Dojo.objects.all(),
        "Ninja":Ninja.objects.all()
    }   
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        dojo_id=request.POST.get('dojo_id')
        Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=Dojo.objects.get(id=dojo_id))
        return redirect('/')
    return redirect('/')


def delete_dojo(request,dojo_id):
    dojo=Dojo.objects.filter(id=dojo_id).first()
    if dojo:
        dojo.delete()
    return redirect('/')
