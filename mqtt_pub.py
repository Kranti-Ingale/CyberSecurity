#Program for MQTT
import paho.mqtt.publish as publish
import sys
import random
import time

broker_url = "localhost"
broker_port = 1883
topic = "test/storeoccupancy"
username = "kranti"
password = "kranti"

while True:
    peoplecount = random.randint(0, 1000)
    if peoplecount >=900:
        print("No of people in IKEA store are overcrowded with: " + str(peoplecount))
        msg="overcrowded with: " + str(peoplecount)
        publish.single(topic, msg, hostname=broker_url, port=broker_port, auth={'username': username, 'password': password})
    else:
        print("No of people in IKEA store is: " + str(peoplecount))
        publish.single(topic, peoplecount, hostname=broker_url, port=broker_port, auth={'username': username, 'password': password})
    time.sleep(5)
