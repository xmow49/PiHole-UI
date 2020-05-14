#!/usr/bin/python3
import os, sys
import requests
import time
from fritzconnection.lib.fritzstatus import FritzStatus
from modules.StatusLED import*

#the script will ping for it, if it's online -> Display on ->if not -> Display off
PiHoleIP = 'http://192.168.178.58/admin/api.php'

pwr1 = open('/home/pi/PiHole-UI/modules/PW.txt', 'r')
FritzPW = pwr1.read()
pwr1.close()

LoopTAG = 1

def CheckIfUp(SystemIP):
    while LoopTAG == 1:
        UPTag = ''
        response = os.system("ping -c 1 " + SystemIP)
        print('System-Ping: ', response)    
        if response == 0:
           UPTag = 1
           HostLEDon()
           f = open("/home/pi/PiHole-UI/modules/UPTag.txt", "w")
           f.write(str(UPTag))
           f.close()
           time.sleep(30.0)
        else:
           UPTag = 0
           HostLEDoff()
           f = open("/home/pi/PiHole-UI/modules/UPTag.txt", "w")
           f.write(str(UPTag))
           f.close()
           time.sleep(30.0)

def PiHoleUp():
    while LoopTAG == 1:
        response = requests.head(PiHoleIP)
        statuscode = response.status_code
        print('PI-Ping: ', response, 'statuscode: ', statuscode)
        if statuscode == 200:
           PiHoleLEDon()
           time.sleep(60.0)
        else:
           PiHoleLEDoff()
           time.sleep(60.0)
      
def FBconnected(FritzPW):
    while LoopTAG == 1:
        fstatus = FritzStatus(address='192.168.178.1', password=FritzPW)
        FON = fstatus.is_linked
        if FON == True:
           FritzOnlineLEDon()
           time.sleep(60.0)
        if FON == False:
           FritzOnlineLEDoff()
           time.sleep(60.0)
