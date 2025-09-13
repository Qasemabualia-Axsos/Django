from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):


    return render (request,'index.html')

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
                return redirect('/home')
        else:
            messages.error(request,'Invalid email or password',extra_tags='login')
            return redirect('/')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')


def home(request):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    user=Users.objects.get(id=request.session['userid'])
    data={
        'user':user,
        'Messages':Messages.objects.all().order_by('-created_at'),
        'comment':Comments.objects.all()
    }
    return render(request,'home.html',data)

def post_msg(request):
    if request.method=='POST':
        user=Users.objects.get(id=request.session['userid'])
        content=request.POST.get('content')
        Messages.objects.create(
            content=content,user=user
        )
        data={
            'user':user,
            'Messages':Messages.objects.all()
        }
        return redirect('/home',data)
    return redirect('/home')

def wall(request):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first', extra_tags='login')
        return redirect('/')
    user=Users.objects.get(id=request.session['userid'])
    data={
        'user':user,
        'Messages':Messages.objects.all(),
        'Comments':Comments.objects.all().order_by('created_at')
    }

    return render (request,'comment.html',data)

def post_comment(request):
    if request.method=='POST':
        user=Users.objects.get(id=request.session['userid'])
        comment=request.POST.get('comment')
        message_id = request.POST.get('message_id')
        message=Messages.objects.get(id=message_id)
        Comments.objects.create(
            comment=comment,user=user,message=message
        )
        data={
            'user':user,
            'Messages':Messages.objects.all(),
            'Comments':Comments.objects.all()
        }
        return redirect ('/wall',data)
    return redirect ('/wall')
