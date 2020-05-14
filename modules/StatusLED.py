#!/usr/bin//python3
import psutil
import time
from gpiozero import LED

AA = LED(5)
BB = LED(6)
CC = LED(13)
DD = LED(18)
EE = LED(17)
FF = LED(27)
GG = LED(22)

def SysStart():
    AA.off()
    BB.off()
    CC.off()
    DD.off()
    EE.off()
    FF.off()
    GG.off()
    time.sleep(0.1)
    AA.on()
    time.sleep(0.5)
    BB.on()
    time.sleep(0.5)
    CC.on()
    time.sleep(0.5)
    DD.on()
    time.sleep(0.5)
    EE.on()
    time.sleep(0.5)
    FF.on()
    time.sleep(0.5)
    GG.on()
    time.sleep(1.0)
    GG.off()
    CC.off()
    time.sleep(0.5)
    FF.off()
    BB.off()
    time.sleep(0.5)
    AA.off()
    EE.off()
    
def ProcessorLED():
    while True:
        picpu = int(psutil.cpu_percent(percpu=False))
        time.sleep(0.5)
        if picpu < 5:
            EE.off()
            FF.off()
            GG.off()
            time.sleep(0.5)
        if picpu < 33 and picpu > 5:
            EE.on()
            FF.off()
            GG.off()
            time.sleep(0.5)
        if picpu > 33 or picpu < 66:
            EE.on()
            FF.on()
            GG.off()
            time.sleep(0.5)
        if picpu > 66:
            EE.on()
            FF.on()
            GG.on()
            time.sleep(0.5)
    
def FritzOnlineLEDon():
    AA.on()
    
def PiHoleLEDon():
    BB.on()
    
def HostLEDon():
    CC.on()
    
def FritzOnlineLEDoff():
    AA.off()
    
def PiHoleLEDoff():
    BB.off()
    
def HostLEDoff():
    CC.off()
