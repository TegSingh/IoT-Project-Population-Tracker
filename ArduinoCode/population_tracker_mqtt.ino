// for Arduino microcontroller

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
const int trigPin = D0;      // trigger pin
const int echoPin = D1;      // echo pin
//const int trigPin = 12;
//const int echoPin = 14;

//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034
#define CM_TO_INCH 0.393701

long duration;
float distanceCm;
int count = 0;
float rangeMax, prev_min_limit, rangeMin, prev_max_limit, previous_distance;
float alarmCount=0;
long compareDuration;
const char* ssid = "17Hundred - Guest";
const char* password = "1700Simcoe1700";
const char* broker_ip_address = "test.mosquitto.org";
const char* outTopic = "test/sensordata";
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  client.setServer(broker_ip_address, 1883);
  // Setting up the wifi
  Serial.println("Connecting to wifi: ");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wifi connected successfully");
}

void loop() {

  if (!client.connected()) {
    connectMQTT();
  }
  client.loop();
  
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance
  distanceCm = duration * SOUND_VELOCITY/2;
 
  count++;

  if (count < 5){
    // Define min and max range for people entering
    rangeMax = distanceCm + (distanceCm*0.05);
    rangeMin = distanceCm - (distanceCm*0.05);
    Serial.println(rangeMax);
    Serial.println(rangeMin);
  }
  
  if (distanceCm > rangeMax || distanceCm < rangeMin){

    // Only register a new person if the distance crosses the 10% tolerance
    prev_min_limit = previous_distance * 0.90;
    prev_max_limit = previous_distance * 1.10;

    // Number of consecutive alarms > 0
    if(alarmCount > 1){

      // Check if tolerance hasnt been breached, still the same person
      if (distanceCm > prev_min_limit && distanceCm < prev_max_limit) {   
        // Increase the alarm count for that distance
        alarmCount++;
      } else {
 
        // Tolerance has been breached, new person
        Serial.print("Alert on ");
        Serial.print(distanceCm);
        Serial.print(" At Time: ");
        Serial.println(duration);
        char message[100];
        snprintf(message, 100, "{\"id\": %d, \"distance\": %f}", count, distanceCm);
        if (distanceCm < 200) {
        client.publish(outTopic, message);  
        }
        // Set the number of alarms to 1
        alarmCount = 1;
      }
    }
    else if (alarmCount == 0){
       // The first time a person is detected
       Serial.print("Alert on ");
       Serial.print(distanceCm);
       Serial.print(" At Time: ");
       Serial.println(duration);
       char message[100];
       snprintf(message, 100, "{\"id\": %d, \"distance\": %f}", count, distanceCm);     if (distanceCm < 200) {
       client.publish(outTopic, message);     
     }   
    }
    alarmCount++;
    previous_distance = distanceCm;
  }
  
  delay(1000);
}

// Method to connect to MQTT
void connectMQTT() {
  
  while (!client.connected()) {
    
    // Create a random client ID
    String clientId = "ESP8266-";
    clientId += String(random(0xffff), HEX);
    Serial.printf("MQTT connecting as client %s...\n", clientId.c_str());
    // Attempt to connect
    if (client.connect(clientId.c_str(), ssid, password)) {
      Serial.println("MQTT connected successfully");
      
      // Publish first announcement
      client.publish(outTopic, "Hello from NodeMCU ESP8266 and Population tracker"); 
      
    } else {
      Serial.printf("MQTT connection insuccessful, Retrying in 5s\n");
      delay(1000);
    }
  }
}
