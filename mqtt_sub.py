import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883
username = "kranti"
password = "kranti"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/storeoccupancy")

def on_message(client, userdata, msg):
    print(msg.topic+"- No of people in the IKEA store now:  "+str(msg.payload))

client = mqtt.Client()
client.username_pw_set(username, password) # set the username and password
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_url, broker_port, 60)

client.loop_forever()
