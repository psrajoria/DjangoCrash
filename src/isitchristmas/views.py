from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    
    return render(request, "isitchristmas/index.html",{
        'answer': now.month==12 and now.day==25
    })
