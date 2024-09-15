from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_satvik(request):
    return HttpResponse("Hello, satvik!")