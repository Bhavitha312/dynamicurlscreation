from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(req):
    return render(req,'myappdemo.html')