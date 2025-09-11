from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html')


def result(request):
    if request.method=="POST":
        data={
        'first_name':request.POST.get('first_name'),
        'dojo_location':request.POST.get('dojo_location'),
        'favorite_language':request.POST.get('favorite_language'),
        'comment':request.POST.get('comment')
    }
        return render (request,'result.html',data)
    return render(request,"index.html")