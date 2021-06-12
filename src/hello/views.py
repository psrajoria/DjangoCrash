from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# def greet(request,name):
#     return httpresponse(f"hello, {name.capitalize()}")


# def greet(request, name, template_name="hello/greet.html"):
#     #context = 
#     return render(request,  template_name, {
#         "name": name.capitalize()
#     })


def greet(request, name):
    #context =
    return render(request,  "hello/greet.html", {
        "name": name.capitalize()
    })
