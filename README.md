# Population Tracking System

This is the repository for the population tracking alarm system. 

## Group members: 

Tegveer Singh - 100730432
Clarissa Branje - 100716458
Toluwanimi Elebute - 100724471

## Table of Content
1. Repository Structure
2. Project Design and Architecture
3. Architecture Design Decisions
4. Deployment Design Decisions
5. Proposal and Report

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

## Project Design and Architecture
The group used HTTP POST Requests to add values in the database. Node-red on the cloud contains HTTP end points that can respond to post, get and delete requests on the respective URLS. Refer to the following screenshot for the flows in the Node-Red
Add image here
The sensor data is posted to the shown URLS. The listener data is sent as messages to these URLS, Function nodes on the Node red parse this data and then generate database queries. These queries then make the changes to the database which is then shown on the Updated Front-end webpage. Refer to the following sequence diagram for a better understanding of the working of our application:
Add image here
**NOTE:** More details about this can be found on the report

## Architecture Design Decisions
1. Multiple alternatives were considered for the implementation of our process. One of the major alternatives included using MQTT as the main communication protocol. This included using an MQTT listener on Node-red which then used function nodes to parse the data to create queries for the database. Refer to the following sequence diagram for a better understanding of this implementation
Add image here
This was discarded since the MQTT listener was missing some values published by the sensor. This reduced the accuracy. To correctly implement this feature, the listener had to be configured to listen to all topics which further created security risks

2. Another major design decision was filtering the sensor values. This was done to remove replication of values and only include the values within an initial range. This was done by setting up tolerance limits and repeated initialization
**NOTE:** More details about this can be found on the report

## Deployment Decisions
1. To ensure secure deployement, SSL certificates using Apache certbot were added to the DNS 
2. Added an adapter script to speed up the process. This adapter script acts as a local MQTT listener and sends post requests using Python library
3. Well formatted README and Links to presentation and Demonstration video have been provided

**NOTE:** More details about this can be found on the report


## Proposal and Report
The Project Proposal and Final Report are contained in this repository
The presentation can be accessed at the following link: 
[Presentation](https://docs.google.com/presentation/d/13aDqTG44b_ZDbJYcGDCTH6TZ6meUKdQAU45xpNVR3zY/edit?usp=sharing)
The video demonstration can be accessed at the following link: 
[Population-Tracker-Video-Demo](https://drive.google.com/file/d/1VBXTdBiyvbmCGMPCLKkyYwZ73hJcRwCL/view?usp=sharing)

