#!/usr/bin/python3

import os, sys
import time
import threading

from multiprocessing import Process
from modules.display import*
from modules.HostChecker import*
from modules.StatusLED import*

SystemIP = '192.168.178.27'
#192.168.178.27 is a sample, use any adress you wish.

FritzPW = 'password'
#Password of your Fritzbox

SysStart()
time.sleep(5.0)

UPTag = ''
dispcounter = 1
FirstStart = 1

Processor = threading.Thread(target=ProcessorLED, daemon=True)
BGCheck1 = threading.Thread(target=CheckIfUp, args=(SystemIP,), daemon=True)
BGCheck2 = threading.Thread(target=PiHoleUp, daemon=True)
BGCheck3 = threading.Thread(target=FBconnected args=(FritzPW,), daemon=True)

Processor.start()
BGCheck1.start()
BGCheck2.start()
BGCheck3.start()

disp.clear()
disp2.clear()

while True:
     if UPTag != "1":
       print('If Uptag!=1')
       p10 = Process(target = LeftGif)
       p11 = Process(target = RightGif)
       p10.start()
       p11.start()
       time.sleep(30.0)
       f = open('/home/pi/PiHole-UI/modules/UPTag.txt', 'r')
       UPTag = f.read()
       p10.terminate()
       p11.terminate()
       if Firstart != 1:
          FirstStart = 1

     if FirstStart == 1 and UPTag == '1':
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
       dispcounter -= 3
