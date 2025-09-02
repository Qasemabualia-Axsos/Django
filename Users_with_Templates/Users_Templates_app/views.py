from django.shortcuts import render,redirect
from .models import Users

# Create your views here.
def index(request):

    data={
        'Users':Users.objects.all()
    }

    return render(request,'index.html',data)

def add_user(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        Name=f'{first_name} {last_name}'
        
        Users.objects.create(Name=Name,Email=email,Age=age if age else None)
    return redirect('/')