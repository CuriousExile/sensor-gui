from django.shortcuts import render
from django.http import HttpResponse
import os
import glob
import time

def index(request):
    context = {
        'graph_data': [20,20,20,20,20,20,20],
        'temperature': 0,
    }
    return render(request, 'pages/index.html', context)

def input(request): 
    return render(request, 'pages/input.html')

