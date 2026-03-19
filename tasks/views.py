from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by("id")
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

def detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})
def contact(request):
    return HttpResponse("This is the contact page")