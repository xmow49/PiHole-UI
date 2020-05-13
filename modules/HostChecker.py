#!/usr/bin/python3
import os, sys

SystemIP = '192.168.178.27'
#192.168.178.27 is a sample, use any adress you wish.
#the script will ping for it, if it's online -> Display on ->if not -> Display off
PiHoleIP = 'pi.hole'

def CheckIfUp():
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
        UPTag = ''
    response = os.system("ping -c 1 " + PiHoleIP)
    print('System-Ping: ', response)    
    if response == 0:
        f = open("/home/pi/PiHole-UI/modules/PiHoleUp.txt", "w")
        f.write(str(UPTag))
        f.close()
    else:
        f = open("/home/pi/PiHole-UI/modules/PiHoleUp.txt", "w")
        f.write(str(UPTag))
        f.close()
