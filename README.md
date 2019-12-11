# aws_iot_esp8266
## Objective:
Reading a sensor using ESP8266 and the Raspberry Pi,  RPI receives the data sent by the ESP8266 and sends it to the AWS IoT server.


![diagrama](https://user-images.githubusercontent.com/39311424/69901853-d090da00-1365-11ea-8d6d-5d817330874e.png)

## Step by step:
1. You need to create a aws account and set up the "Things" that you will use
 (Just follow the instruction ->https://circuitdigest.com/tutorial/getting-started-with-amazon-aws-for-iot-projects)  
    * In the aws Iot you will download the private key, public key and certificate, save this in a safe place. 

1. To connect with the RPI you need to know the ip address, you can use the Wireshark program (using the DHCP filter)

1. Make sure that you and RPI is in the same network 

1. You can connect with the RPI using your linux shell and the ssh command
    * $ ssh pi@ipadress

1. Now you have access to RPI 

1. You need send this to the RPI: privatekey.key, publickey.key, cert.pem and the "aws_server.py"
    * To sent something to the RPI you can use this commmand: $ scp filename.py  pi@ipadress:/home/pi

1. Now you had set up the RPI 

1. You need change in the code your certificate and keys 

1. Connect the ESP8266 in you computer, compile the "http_get.c" (don't forget to change the wifi name and password and the ip address in the code)

1. After this, execute the "aws_server.py"
     * $ python3 aws_server.py 

1. You should see the ADC value in the shell

1. Go to your aws IoT -> tests -> subscribe in a "ESP" topic

1. And that's it, you should see the ADC value in the AWS IoT
