import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import socket
import sys

HOST = '192.168.0.101'   # Symbolic name meaning all available interfaces
PORT = 10000 # Arbitrary non-privileged port
#PORT_tcp = 5000

############## SERVER RPI ##########################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
orig = (HOST, PORT)

try:
    s.bind(orig)
except socket.error as msg:
    print('Bind failed. Error Code : ' , str(msg[0]) , ' Message ' , msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')
##############  END SERVER RPI ##########################

###############SERVIDOR TCP AWS ####################
# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# orig_tcp = (HOST, PORT_tcp)
# tcp.bind(orig_tcp)
# tcp.listen(1)
connflag = False

def on_connect(client, userdata, flags, rc):
     global connflag
     connflag = True
     print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))

def on_log(client, userdata, level, buf):
    print(msg.topic+" "+str(msg.payload))

awshost = "a13f0ppwu2hmq8-ats.iot.us-east-2.amazonaws.com"
awsport = 8883
clientId = "ESP"
thingName = "ESP"
caPath = "./cert/AmazonRootCA1.pem"
certPath = "./cert/9892a36a33-certificate.pem.crt"
keyPath = "./cert/9892a36a33-private.pem.key"

############### END SERVIDOR TCP AWS ####################


while 1==1:
     conn, addr = s.accept()
     print('Connected with ' , addr[0] , ':' , str(addr[1]))
     #now keep talking with the client
     data = conn.recv(1024)
     conn.sendall(data)
     conn.close()
     print(data)
     sleep(0.5)

     #------AWS-----
     mqttc = paho.Client()
     mqttc.on_connect = on_connect
     mqttc.on_message = on_message
     mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath,
     cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
     mqttc.connect(awshost, awsport, keepalive=60)
     mqttc.loop_start()
     #data =125
     if connflag == True:
         mqttc.publish("ADC", data, qos=1)
         print("msg sent: ADC ",data)
     else:
         print("waiting for connection...")


s.close()
tcp.close()
