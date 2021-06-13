from django.shortcuts import render


tasks = ["foo","boo","doo"]

# Create your views here.

def index(request):
    return render(request,"tasks/index.html",{
        'tasks':tasks
    })

def add_task(request):
    return render(request,"tasks/add.html")