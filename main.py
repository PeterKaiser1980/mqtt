# import paho-mqtt
import paho.mqtt.client as mqtt

if __name__ == "__main__":
    print("Hello, World!")
    # mqtt.Client(client_id=””, clean_session = True, userdata = None, protocol = MQTTv311, transport =”tcp”)
    mqtt.Client(client_id='ryzen', clean_session=True, userdata=None, protocol='MQTTv311', transport ='tcp')
    # mqtt.connect(host, port=1883, keepalive=60, bind_address="")
    # mqtt.Client.connect('192.168.0.127')
    mqtt.Client.connect(host='192.168.0.127')
    # mqtt.Client.subscribe('Aussen/#')
