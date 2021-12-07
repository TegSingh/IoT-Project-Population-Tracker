# Population-Tracking-Alarm-System-IoT

## Important Features:

1. This is the source code repository for **Assignment 2** of Design and Analysis of Internet of Things Systems
2. The main focus is on the **design methodology** of Population Tracking Alarm System
3. MQTT is used as for communication using a pub-sub mechanism
4. Used NodeMCU kit with a laser sensor to determine the number people in indoor facilities during COVID

## URLs:

1. **/:** Shows app home page
2. **sensor_data_delete/<int:pk>/** : Invoked on delete button click in home page
3. **api/:** Shows API overview and lists the URLS
4. **api/sensor_data_list/** : Lists all the tuples in the sensor_data model in JSON format
5. **api/sensor_data_detail/<int:pk>/:** Provides detail about on tuple in the model
6. **api/sensor_data_create/**: Adds a tuple to the model by taking in JSON formatted input
7. **api/sensor_data_delete/<int:pk>/**: Deletes the tuple provided in the URL
8. **api/sensor_data_update/<int:pk>/**: Updates some sensor data in case updating is required
