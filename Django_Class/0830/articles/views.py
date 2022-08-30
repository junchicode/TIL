from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple','coco','orange',]
    info = {
        'name':'jlee'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html',{'name':'Alice'})

def dinner(request):
    foods = ['마라','오이','물']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods': foods,
    }
    return render(request, 'dinner.html',context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message =request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)