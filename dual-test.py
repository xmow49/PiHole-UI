#!/usr/bin/python3

import os, sys
import time
import os, sys
import platform
import humanize
import psutil
import requests

from multiprocessing import Process
from fritzconnection.lib.fritzstatus import FritzStatus
from modules.display import*
from modules.HostChecker import*
from modules.StatusLED import*

SystemIP = '192.168.178.27'
#192.168.178.27 is a sample, use any adress you wish.
piface = os.getenv('PIHOLE_OLED_INTERFACE', 'eth0') 

FritzPW = 'password'
#Password of your Fritzbox
fstatus = FritzStatus(address='192.168.178.1', password=FritzPW)

SysStart()

UPTag = ''
dispcounter = 1
FirstStart = 1
loopcount = 0

BGCheck1 = Process(target = CheckIfUP)
BGCheck2 = Process(target = PiHoleUp)
BGCheck3 = Process(target = FBconnected)
BGCheck1.start(SystemIP)
BGCheck2.start()
BGCheck3.start(FritzPW)

ProcessorLED()

disp.clear()
disp2.clear()

while True:
     p12 = Process(target = PiHoleUp)
     p12.start()
     time.sleep(3.0)
     p12.terminate()
     piholefile = open('/home/pi/PiHole-UI/modules/PiHoleUp.txt', 'r')     
     PiHo = piholefile.read()
     FON = fstatus.is_linked
     if Firtstart == 1 or loopcount == 10:
       p7 = Process(target = CheckIfUp)
       p7.start()
       time.sleep(3.0)
       p7.terminate()
       f = open('/home/pi/PiHole-UI/modules/UPTag.txt', 'r')
       UPTag = f.read()
       picpu = int(psutil.cpu_percent(percpu=False))
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
         p5.terminate()
         p6.terminate()
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
       p1.terminate()
       p2.terminate()
       dispcounter += 1

     if dispcounter == 3 and UPTag == '1':
       print('5 Schleife nach start:', dispcounter, UPTag)
       p3 = Process(target = LS2)
       p4 = Process(target = RS2)
       p3.start()
       p4.start()
       time.sleep(8.0)
       p3.terminate()
       p4.terminate()
       dispcounter += 1
     
     if dispcounter == 4 and UPTag == '1':
       print('6 Schleife nach start:', dispcounter, UPTag)
       p8 = Process(target = ClockDisplayL)
       p9 = Process(target = ClockDisplayR)
       p8.start()
       p9.start()
       time.sleep(5.0)
       p8.terminate()
       p9.terminate()
       dispcounter -= 2
       loopcount += 1
