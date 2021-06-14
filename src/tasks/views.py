from django.forms.fields import CharField
from django.http.response import HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=20, label="New Task",
                           widget=forms.TextInput(attrs={'placeholder': 'Task'}))


tasks = []

# Create your views here.


def index(request):
    return render(request, "tasks/index.html", {
        'tasks': tasks
    })


def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            #### To reverse engineer URL
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            render(request, "tasks/add.html", {
                'form': form
            })

    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
    })
