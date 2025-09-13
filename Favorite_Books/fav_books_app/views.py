from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
# Create your views here.
def index(request):

    data={
        'Users':Users.objects.all(),
        'Books':Books.objects.all()
    }

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
        messages.success(request,'Successfully Creat User',extra_tags='register')
        return redirect('/')
    

def login(request):
    if request.method=='POST':
        user=Users.objects.filter(email=request.POST.get('email')).first()
        if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
            request.session['userid']=user.id
            request.session['first_name']=user.first_name
            messages.success(request,'Successfully login',extra_tags='login')
            return redirect ('/success')
        else:
            messages.error(request,'Invalid Email ot Password',extra_tags='login')
            return redirect('/')
    return redirect('/')

def success(request):
    if 'userid' not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    data={
        'Books':Books.objects.all(),
        'user':logged_user
    }
    return render(request,'success.html',data)


def delete(request):
    request.session.flush()
    return redirect('/')

def add_book(request):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    errors=Books.objects.book_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value,extra_tags='add_book')
        return redirect('/success')
    user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.create(
        title=request.POST.get('title'),
        desc=request.POST.get('desc'),
        uploaded_by=user
    )
    book.user_who_like.add(user)
    return redirect('/success')

def add_fav(request,book_id):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.filter(id=book_id).first()

    book.user_who_like.add(user)
    return redirect('success')

def remove_fav(request,book_id):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.filter(id=book_id).first()
    book.user_who_like.remove(user)
    return redirect(f'/books/{book_id}')




def display_book(request,book_id):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.get(id=book_id)
    data={
        'book':book,
        'user':logged_user
    }
    return render (request,'display_book.html',data)

def edit_book(request,book_id):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.get(id=book_id)

    if request.method=='POST':
        
        book.title=request.POST.get('title')
        book.desc=request.POST.get('desc')
        book.save()

        return redirect(f'/books/{book_id}')
    return redirect(f'/books/{book_id}')
    
def delete_book(request,book_id):
    if "userid" not in request.session:
        messages.error(request,'Please log in first',extra_tags='login')
        return redirect('/')
    logged_user=Users.objects.get(id=request.session['userid'])
    book=Books.objects.get(id=book_id)
    if book.uploaded_by.id==request.session['userid']:
        book.delete()
    return redirect('/success')
