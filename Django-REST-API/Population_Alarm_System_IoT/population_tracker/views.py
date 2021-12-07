from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Sensor_data
from django.http import Http404

# import the methods for API request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SensorDataSerializer

# Create your views here.

# Home page to show the number of people entering [list view]
def home(request):
    # Add random data using utility method

    try:
        sensor_data = Sensor_data.objects.all()
        population =  calculate_total_objects()
    except:
        raise Http404()

    context = {"population" : population, "Sensor_data" : sensor_data}
    return render(request, "population_tracker/home.html", context)

# Utility Method to add random data for Testing 
# NOTE: Only use this when testing is needed 
# NOTE: If called in home view, CRUD wont work [can only use admin]
def util_add_random_sensor_data(): 
    person_number = [3, 4, 7, 10, 11, 1, 2, 9, 13]
    distance = [34, 55, 91, 23, 12, 87, 34, 22, 60]
    for i in range(len(person_number)):
        sensor_data_add(person_number[i], distance[i])

# Method to delete data
def sensor_data_delete(request, pk):
    print("Delete method called for ", pk)
    deleted_item = Sensor_data.objects.filter(person_number = pk)
    deleted_item.delete()
    return redirect('home')

# Method to add data
def sensor_data_add(person, distance):
    created_item = Sensor_data(person_number = person, distance = distance)
    created_item.save()

# Method to calculate total number of people
def calculate_total_objects(): 
    return Sensor_data.objects.all().count()

# Following are the API views

# Method for an overview of API urls
@api_view(['GET'])
def apiOverview(request):
    url_patterns = {
        "List" : "/Sensor_data_list/", 
        "Detail" : "/Sensor_data_detail/<int:pk>", 
        "Create" : "/Sensor_data_create/",
        "Update" : "/Sensor_data_update/<int:pk>",
        "Delete" : "/Sensor_data_delete/<int:pk>",
    }
    return Response(url_patterns)

# Method to get list of the sensor data
@api_view(['GET'])
def api_sensor_data_list(request): 
    sensor_data = Sensor_data.objects.all()
    # Serializer shows the JSON data in the correct format as a list
    serializer = SensorDataSerializer(sensor_data, many=True)
    return Response(serializer.data)

# Method to detail one sensor_data
@api_view(['GET'])
def api_sensor_data_detail(request, pk): 
    sensor_data = Sensor_data.objects.get(person_number = pk)
    
    # Raise an exception if element does not exist
    if not Sensor_data.objects.get(person_number = pk):
        raise Http404()

    serializer = SensorDataSerializer(sensor_data, many=False)
    return Response(serializer.data)

# Method to create a tuple using JSON
@api_view(['POST'])
def api_sensor_data_create(request): 
    serializer = SensorDataSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# Method to delete a row in Sensor_data
@api_view(['DELETE'])
def api_sensor_data_delete(request, pk): 
    sensor_data = Sensor_data.objects.get(person_number = pk)
    sensor_data.delete()

    return redirect('home')


# Method to update a row in Sensor_data
@api_view(['POST'])
def api_sensor_data_update(request, pk): 
    sensor_data = Sensor_data.objects.get(person_number = pk)
    serializer = SensorDataSerializer(instance = sensor_data, data = request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response("Item updated successfully")

