#!/usr/bin/python3

FrzitzPW = 'password' 
#Password of your Fritzbox

#initialisation for Fritz.Box API / IP and Password needs to be customized:
def FritzStatus:
  fs = FritzStatus(address='192.168.178.1', password=FritzPW)
  
def FritzHosts:
  fh = FritzHosts(address='192.168.178.1', password=FritzPW)
  
def FritzWLAN:
  fw = FritzWLAN(address='192.168.178.1', password=FritzPW)
  
def Fritzcall:
  fc = FritzCall(address='192.168.178.1', password=FritzPW)
