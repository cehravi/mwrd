from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def test(request):
    return HttpResponse("Hello world")
