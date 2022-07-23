import paho.mqtt.subscribe as subscribe
import time

msg = subscribe.simple("Aussen/#", hostname="192.168.0.127")
while True:
    msg = subscribe.simple("Aussen/BME280/temperature", hostname="192.168.0.127")
    print("%s %s" % (msg.topic, msg.payload))
    msg = subscribe.simple("Aussen/DHT22/temperature", hostname="192.168.0.127")
    print("%s %s" % (msg.topic, msg.payload))
    time.sleep(1)