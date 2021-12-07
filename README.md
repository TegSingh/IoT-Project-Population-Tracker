# Population Tracking System

This is the repository for the population tracking alarm system. 

## Group members: 

Tegveer Singh - 100730432
Clarissa Branje - 100716458
Toluwanimi Elebute - 100724471

## Repostory Structure

### 1. Arduino-Code
This contains the arduino code. Compile and upload the sketch to get sensor values

### 2. Front-end
This directory contains the php file that can also be located at the following link:\
[Population-Tracking-System](https://www.tegveersingh.xyz/index.php)\
The file reads the cloud database on PHPMyAdmin Digital Ocean and displays it in a table format \
The password has been removed \
This file has been retrieved from the **Cloud DNS www directory** 

### 3. Scripts
This directory contains a script for reading mqtt published values and sending HTTP requests to the Node-red. For more details refer to the Documentation

### 4. Django-REST-API
This is the code for Assignment 2. This contains a miniature API that was used for initial testing and development. Refer to the following instructions to run this project. \
**NOTE:** This is not important for the final functionality of the project \
**NOTE:** The values in the database are generated locally, so it wont show anything on the first run

### Instructions

1. Run the following commands in windows
```cmd
py -m virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
```

2. Navigate into Django-REST-API directory

3. Navigate into the Population_Alarm_System_IoT directory

4. Run the following command
python3 manage.py runserver
Once this command is running, navigate to the prompted link to check the project

5. Refer to the README and Report in the directory for further instructions

### 5. Documentation
This section contains the Project Proposal and Final Report. The video Demonstration file has also been added to this section
