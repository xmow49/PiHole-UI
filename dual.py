#!/usr/bin/python3

import os
import platform
import time
import humanize
import psutil
import requests
from threading import Thread

#imports for Fritz.Box
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzwlan import FritzWLAN
from fritzconnection.lib.fritzcall import FritzCall

#imports for Display
from luma.core.interface.serial import i2c
from luma.core.sprite_system import framerate_regulator
from luma.oled.device import ssd1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageSequence
from datetime import datetime

interface = os.getenv('PIHOLE_OLED_INTERFACE', 'wlan0')                           #Network interface to retrieve the IP address / use wlan0 for pizero / eth0 for pi
mount_point = os.getenv('PIHOLE_OLED_MOUNT_POINT', '/')                           #Mount point for disk usage info
fritzconnection = FritzConnection(address='192.168.178.1', password='password')   #initialisation for Fritz.Box API / IP and Password may need to be changed.
fc = FritzStatus(address='192.168.178.1', password='password')
fh = FritzHosts(address='192.168.178.1', password='password')
fw = FritzWLAN(address='192.168.178.1', password='password')
fc = FritzCall(address='192.168.178.1', password='password')

serial = i2c(port=1, address=0x3C)
disp = ssd1306(serial)
serial2 = i2c(port=0, address=0x3C)
disp2 = ssd1306(serial2)

width = disp.width
height = disp.height
disptimer = 0
inforefreshtag = 1
pindexleft = 0
pindexright = 0

disp.clear()
disp2.clear()

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()        #truetype('./SF_Pixelate.ttf', 10)

sleep = 4  # seconds

hostname = platform.node()

threadlist  = {}
def cb(id, currtime):
    t = threadlist[id]
    d = currtime - t.starttime
    if d > 10:
        return True
    else:
        return False
    
def function1(arg1, arg2, arg3, duration, cb, threadid):
    t_end = time.time() + duration
    while time.time() < t_end:
        #do some stuff
        if cb(threadid, time.time()):
            break

for i in range(100):
    t = Thread(target = function1, args=(arg1, arg2, arg3, 10, cb, i))
    threadlist[id] = {"starttime": time.time(), "thread": t}
    t.start()

And to check:

time.sleep(15)
for item in threadlist.values():
    print(item.thread.is_alive())

#class LeftScreen:
def LS1:           
    #1st Screen CPU/RAM/Uptime..if elapsed_seconds >= 5 and elapsed_seconds <= 10: 
   addr = psutil.net_if_addrs()[interface][0]
   draw.text((0, 0), "Pi-hole %s" % addr.address.rjust(15), font=font, fill=255)
   uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
   draw.text((0, 12), "Up: %s" % humanize.naturaltime(uptime), font=font, fill=255)
   draw.text((0, 22), "    %.1f %.1f %.1f" % os.getloadavg(), font=font, fill=255)
   cpu = int(psutil.cpu_percent(percpu=False))
   draw.text((0, 34), "CPU", font=font, fill=255)
   draw.rectangle((26, 34, 126, 34 + 6), outline=255, fill=0)            
   draw.rectangle((26, 34, 26 + cpu, 34 + 6), outline=255, fill=255)
   mem = int(psutil.virtual_memory().percent)
   draw.text((0, 44), "RAM", font=font, fill=255)
   draw.rectangle((26, 44, 126, 44 + 6), outline=255, fill=0)
   draw.rectangle((26, 44, 26 + cpu, 44 + 6), outline=255, fill=255)
   disk = int(psutil.disk_usage(mount_point).percent)
   draw.text((0, 54), "Disk", font=font, fill=255)
   draw.rectangle((26, 54, 126, 54 + 6), outline=255, fill=0)            
   draw.rectangle((26, 54, 26 + disk, 54 + 6), outline=255, fill=255 )
   disp.display(image)
def LS2:
    #2nd Screen PiHole Infos...
    try:                                                
        req = requests.get('http://pi.hole/admin/api.php')
        data = req.json()
        draw.text((0, 0), "Pi-hole (%s)" % data["status"], font=font, fill=255)
        draw.line((0, 12, width, 12), fill=255)
        draw.text((0, 22), "Blocked: %d (%d%%)" % (data["ads_blocked_today"], data["ads_percentage_today"]), font=font, fill=255)                
        draw.text((0, 32), "Queries: %d" % data["dns_queries_today"], font=font, fill=255)
        draw.line((0, 50, width, 50), fill=255)
        draw.text((0, 54), "Blocklist: %d" % data["domains_being_blocked"], font=font, fill=255)                
    except:
        draw.text((0, 0), "ERROR!", font=font, fill=255)
        disp.display(image)

#class RightScreen:
def RS1:                   
    #1st Fritzbox screen (uptime, up-/download) elapsed_seconds >= 10 and elapsed_seconds <= 15:
    fbuptime = fc.str_uptime
    fbspeed = fc.str_max_bit_rate
    draw.text((0, 0), "Fritz.Box infos: ", font=font, fill=255)
    draw.line((0, 10, width, 10), fill=255)
    draw.text((0, 14), "Uptime: ", font=font, fill=255)
    draw.text((64, 14), fbuptime, font=font, fill=255)
    draw.text((0,26), "Upload-Speed: ", font=font, fill=255)
    draw.text((50,36), fbspeed[0], font=font, fill=255)
    draw.text((0,46), "Download-Speed: ", font=font, fill=255)
    draw.text((50,56), fbspeed[1], font=font, fill=255)
    disp2.display(image)
def RS2:
    #2nd Fritzbox screen
    hosts = fh.host_numbers
    ssid = fw.ssid
    missedcalls = fc.get_missed_calls(update=true, num=10, days=7)
    draw.text((0, 0), "Fritz.Box infos: ", font=font, fill=255)
    draw.line((0, 10, width, 10), fill=255)
    draw.text((0, 14), "SSID: ", font=font, fill=255)
    draw.text((64, 14), ssid, font=font, fill=255)
    draw.text((0,26), "Hosts: ", font=font, fill=255)
    draw.text((50,36), hosts, font=font, fill=255)
    draw.text((0,46), "missed calls: ", font=font, fill=255)
    draw.text((50,56), missedcalls, font=font, fill=255)
    disp2.display(image)
        
#class GifLeft:
def LeftGif:
        #Gifscreen for left display: elapsed_seconds >= 15 and elapsed_seconds <= 17:
    regulator = framerate_regulator(fps=10)
    left_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'res', 'Fallin-L.gif'))
    left = Image.open(left_path)
    size = [128, 64]
    posn = (0, 0)
    timecheck = time.time()            
    while time.time() <= timecheck + giftimer:
         for frame in ImageSequence.Iterator(left):
             with regulator:
                  background = Image.new("RGB", disp.size, "white")
                  background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                  disp.display(background.convert("1"))
             if time.time() >= timecheck + giftimer:
                  break
      
#class GifRight:
def RightGif:
        #Gifscreen for right display: elapsed_seconds >= 15 and elapsed_seconds <= 17:
    regulator2 = framerate_regulator(fps=10)
    regulator2 = framerate_regulator(fps=10)
    right_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'res', 'Fallin-R.gif'))
    right = Image.open(right_path)
    size = [128, 64]
    posn = (0, 0)
    timecheck = time.time()            
    while time.time() <= timecheck + giftimer:
         for frame in ImageSequence.Iterator(right):
             with regulator:
                 background = Image.new("RGB", disp.size, "white")
                 background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                 disp2.display(background.convert("1"))
             if time.time() >= timecheck + giftimer:
               break

time.sleep(sleep)

if disptimer ==0 and disptimer <= 5:
    screen1 = threading.Timer(5, LS1)
    screen2 = threading.Timer(5, RS1)
    screen1.start()
    screen2.start()

elapsed_seconds += 1

except (KeyboardInterrupt, SystemExit):
    print("Exiting...")
