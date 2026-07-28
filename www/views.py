from django.shortcuts import render

from www.models import *


def index(request):
    return render(request, 'index.html')

def test1(request):
    return render(request, 'one.html')
def test2(request):
    return render(request, 'test2.html')
def test3(request):
    return render(request, 'test3.html')
def test4(request):
    return render(request, 'test4.html')
def test5(request):
    return render(request, 'test5.html')
# Create your views here.
