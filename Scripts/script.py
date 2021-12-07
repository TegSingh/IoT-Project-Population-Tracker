import paho.mqtt.client as mqtt
import requests
import json

#The callback for when the client receive a connack response from the server
def on_connect(client, uesrdata, flags, rc):
    print ("connected with result code " +str(rc))
    client.subscribe("test/sensordata")

def on_message(client, userdata, msg):
    print(msg.payload)
    phpjson = str(msg.payload)
    phpjsonfilter = phpjson[2:len(phpjson)-1]
    print(phpjsonfilter)
    phpjsonfilterobject = json.loads(phpjsonfilter)
    print(phpjsonfilterobject)

    url_cloud = "https://www.tegveersingh.xyz:1880/add"
    r = requests.post(url_cloud, data = phpjsonfilterobject, verify = False)
    if r.ok:
        print(r.status_code)
    else:
        pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect ("test.mosquitto.org", 1883, 60)
client.loop_forever()