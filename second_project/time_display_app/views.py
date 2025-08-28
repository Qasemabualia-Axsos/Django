from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return redirect('time_display/')

def time_display(request):
    data={
       'time':  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render(request,'index.html',data)