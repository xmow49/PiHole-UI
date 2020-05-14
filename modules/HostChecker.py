#!/usr/bin/python3
import os, sys
import requests
import time
import RPi.GPIO as GPIO
from fritzconnection.lib.fritzstatus import FritzStatus

#the script will ping for it, if it's online -> Display on ->if not -> Display off
PiHoleIP = 'http://192.168.178.58/admin/api.php'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.OUT)   #physical Pin-Nr.35 -> Indicator for PiHole Service Running


def CheckIfUp(SystemIP):
    UPTag = ''
    response = os.system("ping -c 1 " + SystemIP)
    print('System-Ping: ', response)    
    if response == 0:
        f = open("/home/pi/PiHole-UI/modules/UPTag.txt", "w")
        f.write(str(UPTag))
        f.close()
    else:
        f = open("/home/pi/PiHole-UI/modules/UPTag.txt", "w")
        f.write(str(UPTag))
        f.close()

def PiHoleUp():
    response = requests.head(PiHoleIP)
    statuscode = response.status_code
    print('PI-Ping: ', response, 'statuscode: ', statuscode)
    if statuscode == 200:
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(6, GPIO.LOW)
      
def FBconnected(FritzPW):
    fstatus = FritzStatus(address='192.168.178.1', password=FritzPW)
    FON = fstatus.is_linked
    tim
    if FON == True:
       FritzOnlineLEDon()
    if FON == False:
       FritzOnlineLEDoff()
