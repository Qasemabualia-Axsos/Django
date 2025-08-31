from django.shortcuts import render,redirect,HttpResponse
import random
from datetime import datetime
# Create your views here.


def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'act' not in request.session:
        request.session['act']=[]

    
    context={
        'farm':(10,20),
        'cave':(10,20),
        'house':(10,20),
        'quest':(-50,50),
        'gold':request.session['gold'],
        'act':request.session['act']
    }

    return render (request,'index.html',context)

def process_money(request):
    if request.method=='POST':
        place=request.POST.get('place')

        ranges={
            'farm':(10,20),
            'cave':(10,20),
            'house':(10,20),
            'quest':(-50,50),
        }
        if place in ranges:
            low,high=ranges[place]
            gold_earned=random.randint(low,high)
            request.session['gold']+=gold_earned
            time=datetime.now().strftime("%Y/%m/%d %I:%M %p")
            
            if gold_earned>=0:
                Activities=f"You entered a {place} and earned {gold_earned}.({time})"
            else:
                Activities=f"You failed a {place} and lost {gold_earned} gold.Ouch.({time})"
        
            request.session['act'].append(Activities)
            
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect ('/')