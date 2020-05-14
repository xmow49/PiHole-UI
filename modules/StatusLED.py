#!/usr/bin//python3
import RPi.GPIO as GPIO
import psutil
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)  #physical Pin-Nr.11 -> Indicator for CPU Usage under 33%
GPIO.setup(27, GPIO.OUT)  #physical Pin-Nr.13 -> Indicator for CPU Usage between 33% and 66%
GPIO.setup(22, GPIO.OUT)  #physical Pin-Nr.15 -> Indicator for CPU Usage above 66%
GPIO.setup(5, GPIO.OUT)   #physical Pin-Nr.33 -> Indicator for Fritzbox Online
GPIO.setup(6, GPIO.OUT)   #physical Pin-Nr.35 -> Indicator for PiHole Service Running
GPIO.setup(13, GPIO.OUT)  #physical Pin-Nr.37 -> Indicator for Host (HostChecker.py) online
GPIO.setup(18, GPIO.OUT)  #physical Pin-Nr.12 -> Indicator for Pi is On

CPUcheck = 1

def SysStart():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW) 
    GPIO.output(18, GPIO.LOW)
    GPIO.setup(17, GPIO.LOW)
    GPIO.setup(27, GPIO.LOW)
    GPIO.setup(22, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(17, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(27, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(22, GPIO.HIGH)
    time.sleep(1.)
    GPIO.setup(22, GPIO.LOW)
    GPIO.setup(13, GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(27, GPIO.LOW)
    GPIO.setup(26, GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(17, GPIO.LOW)
    GPIO.setup(5, GPIO.LOW)
    
def ProcessorLED():
    while CPUCheck == 1:
        picpu = int(psutil.cpu_percent(percpu=False))
        time.sleep(0.5)
        if picpu < 5:
            GPIO.setup(17, GPIO.LOW)
            GPIO.setup(27, GPIO.LOW)
            GPIO.setup(22, GPIO.LOW)
        if picpu < 33 and picpu > 5:
            GPIO.setup(17, GPIO.HIGH)
            GPIO.setup(27, GPIO.LOW)
            GPIO.setup(22, GPIO.LOW)
        if picpu > 33 or picpu < 66:
            GPIO.setup(17, GPIO.HIGH)
            GPIO.setup(27, GPIO.LOW)
            GPIO.setup(22, GPIO.LOW)
        if picpu > 66:
            GPIO.setup(17, GPIO.HIGH)
            GPIO.setup(27, GPIO.HIGH)
            GPIO.setup(22, GPIO.HIGH)      
    
def FritzOnlineLEDon():
    GPIO.output(5, GPIO.HIGH)
    
def PiHoleLEDon():
    GPIO.output(6, GPIO.HIGH)
    
def HostLEDon():
    GPIO.output(13, GPIO.HIGH)  
    
def FritzOnlineLEDoff():
    GPIO.output(5, GPIO.LOW)
    
def PiHoleLEDoff():
    GPIO.output(6, GPIO.LOW)
    
def HostLEDoff():
    GPIO.output(13, GPIO.LOW)
