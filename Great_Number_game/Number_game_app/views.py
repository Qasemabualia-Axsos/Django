from django.shortcuts import render,redirect
import random
# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number']=random.randint(1,100)
    
    guess=None

    if request.method=='POST':
        guess=int(request.POST.get("number"))
        request.session['guess']=guess
        return redirect('/')
    guess=request.session.get('guess')
    context={
        'number':request.session['number'],
        'guess':guess

    }
    return render(request,'index.html',context)


def play_again(request):
    request.session.flush()
    return redirect('/')