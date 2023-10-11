from django.shortcuts import render
from django.http import HttpResponse
import os
import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')  # Opens the temperature device file
    lines = f.readlines()  # Returns the text
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def index(request):
    context = {
        'graph_data': [24.2, 24.2, 24.2, 24.8, 22.1, 26.1, 27.3],
        'temperature': read_temp(),
    }
    
    return render(request, 'pages/index.html', context)

def input(request):
    
    return render(request, 'pages/input.html')

