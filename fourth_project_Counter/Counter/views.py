from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
    data={
            'count':request.session['count']
        }
    return render(request,'index.html',data)

def destrou_session(request):
    request.session.clear()