from django.db import models
from home.services.sensorservice import SensorApiService

def reduce_data_in_temperature_only(data, target_client):
    temperatures = []
    for entry in data:
        sourcename = entry.get('sourcename')
        if sourcename == target_client:
            temperatures.append(entry.get('temperature'))
    return temperatures