from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.
def shows(request):
    data={
        'Shows':Shows.objects.all()
    }
    return render (request,'show.html',data)



def index(request):
    if request.method=='POST':
        errors=Shows.objects.show_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/shows/new')
        show= Shows.objects.create(
            title=request.POST.get('title'),
            network=request.POST.get('network'),
            release_date=request.POST.get('release_date'),
            description=request.POST.get('description')
            )
        request.session['title']=show.title
        messages.success(request,'Successfully Create Show')
        return redirect('/shows/new')
    return render (request,'index.html')


def action_show(request,num):
    show=Shows.objects.filter(id=num).first()
    time=datetime.now()
    if request.method=='POST':
        show_id=request.POST.get('id')
        if show_id:
         show.add(*show_id)
        return redirect('/shows/')
    data={
        'Shows':Shows.objects.all(),
        'show':show,
        'time':time
    }
    return render(request,'view.html',data)

def action_edit(request,num):
    show=Shows.objects.filter(id=num).first()
    time=datetime.now()
    if request.method=='POST':
        errors=Shows.objects.show_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/shows/num/edit')
        show= Shows.objects.create(
            title=request.POST.get('title'),
            network=request.POST.get('network'),
            release_date=request.POST.get('release_date'),
            description=request.POST.get('description')
            )
        show_id=request.POST.get('id')
        if show_id:
         show.add(*show_id)
        return redirect('/shows/num/edit')
    data={
        'Shows':Shows.objects.all(),
        'show':show,
        'time':time
    }
    return render(request,'edit.html',data)


def update(request,num):
    show=Shows.objects.filter(id=num).first()
    if request.method=='POST':
        show.title=request.POST.get('title')
        show.network=request.POST.get('network')
        show.release_date=request.POST.get('release_date')
        show.description=request.POST.get('description')
        show.save()
        messages.success(request,'Show Updated Successfylly')
        return redirect(f'/shows/{num}/edit')
    data={
        'show':show,
        'num':show.id
    }
    return render(request,'edit.html' ,data)



def delete(request,num):
    show=Shows.objects.filter(id=num).delete()
    return redirect ("/shows/")
    