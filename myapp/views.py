from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def index(request) -> HttpResponse:
    return render(request, "index.html")

def todos(request) -> HttpResponse :
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

