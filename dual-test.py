#!/usr/bin/python3

import os, sys
import time

import os, sys
import platform
import humanize
import psutil
import requests
import RPi.GPIO as GPIO

from multiprocessing import Process
from fritzconnection.lib.fritzstatus import FritzStatus
from modules.display import*
from modules.HostChecker import*
from modules.StatusLED import*


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)  #physical Pin-Nr.12 -> Indicator for Pi is On
GPIO.output(18, GPIO.HIGH)

piface = os.getenv('PIHOLE_OLED_INTERFACE', 'eth0') 
picpu = int(psutil.cpu_percent(percpu=False))

FritzPW = 'password'
#Password of your Fritzbox
fstatus = FritzStatus(address='192.168.178.1', password=FritzPW)
FON = fstatus.is_linked

p12 = Process(target = CheckIfUp)
p12.start()
time.sleep(10.0)
piholefile = open('/home/pi/PiHole-UI/modules/PiHoleUp.txt', 'r')


UPTag = ''
dispcounter = 1
FirstStart = 1
loopcount = 0

PiON = 1
PiHo = piholefile.read()
FBon = FON
CPU33 = ''
CPU66 = ''
CPU100 = ''

disp.clear()
disp2.clear()

while True:
     if Firtstart == 1 or loopcount == 10:
       p7 = Process(target = CheckIfUp)
       p7.start()
       time.sleep(15.0)
       f = open('/home/pi/PiHole-UI/modules/UPTag.txt', 'r')
       UPTag = f.read()
#      os.remove('/home/pi/PiHole-UI/modules/UPTag.txt')
       p7.terminate()
       if UPTag == "1":
         FirstStart = 1     
       if loopcount == 10:
         loopcount -= 9

     
     if UPTag != "1":
       p10 = Process(target = LeftGif)
       p11 = Process(target = RightGif)
       p10.start()
       p11.start()
       time.sleep(60.0)
       p12 = Process(target = CheckIfUp)
       p12.start()
       time.sleep(10.0)
       f = open('/home/pi/PiHole-UI/modules/UPTag.txt', 'r')
       UPTag = f.read()
#      os.remove('/home/pi/PiHole-UI/modules/UPTag.txt')
       p12.terminate()
       p10.terminate()
       p11.terminate()
       if Firstart != 1:
         FirstStart = 1

     if dispcounter == 1 and UPTag == '1':
       if FirstStart == 1:
         print('2 Schleife nach start:', dispcounter, UPTag)
         p5 = Process(target = LeftLogo)
         p6 = Process(target = RightLogo)
         p5.start()
         p6.start()
         time.sleep(5.0)
         p5.kill()
         p6.kill()
         dispcounter += 1
         FirstStart -= 1
       else:
         dispcounter = 2

     if dispcounter == 2 and UPTag == '1':
       print('3 Schleife nach start:', dispcounter, UPTag)
       p1 = Process(target = LS1)
       p2 = Process(target = RS1)
       p1.start()
       p2.start()
       time.sleep(8.0)
       p1.kill()
       p2.kill()
       dispcounter += 1

     if dispcounter == 3 and UPTag == '1':
       print('5 Schleife nach start:', dispcounter, UPTag)
       p3 = Process(target = LS2)
       p4 = Process(target = RS2)
       p3.start()
       p4.start()
       time.sleep(8.0)
       p3.kill()
       p4.kill()
       dispcounter += 1
     
     if dispcounter == 4 and UPTag == '1':
       print('6 Schleife nach start:', dispcounter, UPTag)
       p8 = Process(target = ClockDisplayL)
       p9 = Process(target = ClockDisplayR)
       p8.start()
       p9.start()
       time.sleep(5.0)
       p8.kill()
       p9.kill()
       dispcounter -= 2
       loopcount += 1
