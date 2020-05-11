#!/usr/bin/python3

import os, sys
import time
from multiprocessing import Process
from modules.display import*
from modules.HostChecker import CheckIfUp

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
            f = open("./modules/UPTag.txt", "r")
            UPTag = f.read()
            os.remove("./modules/UPTag.txt") 
            p7.kill()
            if UPTag == 1:
               p5.kill()
               p6.kill()
            if UPTag != "1":
               p5 = Process(target = LeftGif)
               p6 = Process(target = RightGif)
               p5.start()
               p6.start()
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

 #    if dispcounter == 3 and UPTag == '1':
 #          print('4 Schleife nach start:', dispcounter, UPTag)
 #          p5 = Process(target = LeftGif)
 #          p6 = Process(target = RightGif)
 #          p5.start()
 #          p6.start()
 #          time.sleep(14.4)
 #          p5.kill()
 #          p6.kill()
 #          dispcounter += 1

     if dispcounter == 3 and UPTag == '1':
            print('5 Schleife nach start:', dispcounter, UPTag)
            p3 = Process(target = LS2)
            p4 = Process(target = RS2)
            p3.start()
            p4.start()
            time.sleep(5.0)
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
