#!/usr/bin/python3
import os, sys

SystemIP = '192.168.178.27'
#192.168.178.27 is a sample, use any adress you wish.
#the script will ping for it, if it's online -> Display on ->if not -> Display off

def CheckIfUp():
    UPTag = ''
    response = os.system("ping -c 1 " + SystemIP)
    print('System-Ping: ', response)
    if response == 0:
        UPTag = 1
        f = open("UPTag.txt", "w")
        f.write(str(UPTag))
        f.close()
    else:
        UPTag = 0
        f = open("UPTag.txt", "w")
        f.write(str(UPTag))
        f.close()
