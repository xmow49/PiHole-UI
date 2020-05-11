#!/usr/bin/python3

import os, sys
import time
from multiprocessing import Process

#imports for Display
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from modules.display import*
from modules.HostChecker import CheckIfUp

serial = i2c(port=1, address=0x3C)
disp = ssd1306(serial)
serial2 = i2c(port=0, address=0x3C)
disp2 = ssd1306(serial2)

width = disp.width
height = disp.height

UPTag = ''
dispcounter = 1
FirstStart = 1
loopcount = 0

disp.clear()
disp2.clear()

while True:
     if UPTag != '1' or loopcount == 100:
            p7 = Process(target = CheckIfUp)
            p7.start()
            time.sleep(2.0)
            f = open("UPTag.txt", "r")
            UPTag = f.read()
            os.remove("UPTag.txt") 
            p7.kill()
            if UPTag != "1":
              time.sleep(30.0)
            if loopcount == 100:
              loopcount -= 99

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
            time.sleep(5.0)
            p1.kill()
            p2.kill()
            dispcounter += 1

     if dispcounter == 3 and UPTag == '1':
           print('4 Schleife nach start:', dispcounter, UPTag)
           p5 = Process(target = LeftGif)
           p6 = Process(target = RightGif)
           p5.start()
           p6.start()
           time.sleep(14.4)
           p5.kill()
           p6.kill()
           dispcounter += 1

     if dispcounter == 4 and UPTag == '1':
            print('5 Schleife nach start:', dispcounter, UPTag)
            p3 = Process(target = LS2)
            p4 = Process(target = RS2)
            p3.start()
            p4.start()
            time.sleep(5.0)
            p3.kill()
            p4.kill()
            dispcounter += 1

     if dispcounter == 5 and UPTag == '1':
            print('6 Schleife nach start:', dispcounter, UPTag)
            p8 = Process(target = ClockDisplayL)
            p9 = Process(target = ClockDisplayR)
            p8.start()
            p9.start()
            time.sleep(5.0)
            p8.kill()
            p9.kill()
            dispcounter -= 3
            loopcount += 1
