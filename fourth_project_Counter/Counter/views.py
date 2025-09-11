from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    else:
        request.session['count']+=1

    context={
        'count': request.session['count'],
        'num':request.session.get('num')
    }
    return render(request,'index.html',context)


def destroy(request):
    del request.session['count']
    return redirect('/')


def increment_by_2(request):
    request.session['count']=request.session.get('count',0)+1
    return redirect('/')


def incremet_by_user(request):
    if request.method=='POST':
        num= int(request.POST.get('num',0))
        request.session['count'] = request.session.get('count',0)+ num-1
    return redirect('/')