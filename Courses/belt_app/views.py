# Create your views here.
from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
    data={
        'Users': Users.objects.all()
    }
    return render (request,'index.html',data)

def register(request):
    if request.method=='POST':
        errors=Users.objects.user_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value,extra_tags='register')
            return redirect('/')

        else:
            password=request.POST.get('password')
            pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    
        Users.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                password=pw_hash
        )
        request.session['first_name']=request.POST.get('first_name')
        messages.success(request,'Successfully create User',extra_tags='register')
        return redirect('/')


def login(request):
    if request.method=='POST':
        user=Users.objects.filter(email=request.POST.get('email')).first()
        
        if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
                request.session['userid']=user.id
                request.session['first_name']=user.first_name
                messages.success(request,'Successfully logged in !',extra_tags='login')
                return redirect('/success')
        else:
            messages.error(request,'Invalid email or password',extra_tags='login')
            return redirect('/')
    return redirect('/')

def success(request):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    data={
        'user':logged_user,
        'Descriptions':Descriptions.objects.all(),
        'Courses':Courses.objects.all(),
    }
    return render(request,'success.html',data)

def add_course(request):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        description=Descriptions.objects.create(
            description=description)
        Courses.objects.create(
            name=name,
            description=description
        )
        return redirect ('/success')
    return redirect ('/success')

def delete_page(request,course_id):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    course=Courses.objects.get(id=course_id)
    data={
        'user':logged_user,
        'course':course,
    }
    return render (request,"delete.html",data)


def delete_course(request,course_id):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    course=Courses.objects.get(id=course_id)
    course.delete()
    return redirect ('/success')



    
