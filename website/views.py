from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import requests
    


def index(request):
    # return HttpResponse("<h1 style='color:red'>index</h1>")
    context ={"randint":randint(0,100)}
    return render(request, "website/index.html", context)

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")
    
    