from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("sensor_data_delete/delete/<int:pk>", views.sensor_data_delete, name="sensor_data_delete"), 
    path("api/", views.apiOverview, name="apiOverview"), 
    path("api/sensor_data_list", views.api_sensor_data_list, name="sensor_data_list"),
    path("api/sensor_data_detail/<int:pk>", views.api_sensor_data_detail, name="sensor_data_detail"),
    path("api/sensor_data_create/", views.api_sensor_data_create, name="sensor_data_create"),
    path("api/sensor_data_delete/<int:pk>", views.api_sensor_data_delete, name="sensor_data_delete"),
    path("api/sensor_data_update/<int:pk>", views.api_sensor_data_update, name="sensor_data_update"),
    
]
