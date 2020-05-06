#!/usr/bin/python3

import os
import platform
import time

import humanize
import psutil
import requests

#imports for Fritz.Box
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzstatus import FritzStatus

#imports for Display
from luma.core.interface.serial import i2c
from luma.core.sprite_system import framerate_regulator
from luma.oled.device import ssd1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageSequence
from datetime import datetime


# Network interface to retrieve the IP address / use wlan0 for pizero / eth0 for pi
interface = os.getenv('PIHOLE_OLED_INTERFACE', 'wlan0')
# Mount point for disk usage info
mount_point = os.getenv('PIHOLE_OLED_MOUNT_POINT', '/')
# initialisation for Fritz.Box API / IP and Password may need to be changed.
fritzconnection = FritzConnection(address='192.168.178.1', password='password')
fc = FritzStatus(address='192.168.178.1', password='password')

try:
    serial = i2c(port=1, address=0x3C)
    disp = ssd1306(serial)
    serial2 = i2c(port=0, address=0x3C)
    disp2 = ssd1306(serial2)
    is_noop = False
except FileNotFoundError:
    # The error is probably due to this script being run on a system that does
    # not have an OLED connected. In this case, we create fake objects to
    # render the result in the console.
    from image_noop import NoopDisplay, NoopImage, InMemoryImageDraw

    disp = NoopDisplay()
    is_noop = True

width = disp.width
height = disp.height

giftimer = 2

disp.clear()

if is_noop:
    image = NoopImage()
    draw = InMemoryImageDraw(image)
    font = None
else:
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()        #truetype('./SF_Pixelate.ttf', 10)

sleep = 1  # seconds

hostname = platform.node()

try:
    elapsed_seconds = 0
    while True:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        if elapsed_seconds == 17:
            elapsed_seconds = 0

        if elapsed_seconds >= 5 and elapsed_seconds <= 10:
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
            
        elif elapsed_seconds >= 10 and elapsed_seconds <= 15:
            fbuptime = fc.str_uptime
            fbspeed = fc.str_max_bit_rate
            draw.text((0, 0), "Fritz.Box informations: ", font=font, fill=255)
            draw.line((0, 10, width, 10), fill=255)
            draw.text((0, 14), "Uptime: ", font=font, fill=255)
            draw.text((64, 14), fbuptime, font=font, fill=255)
            draw.text((0,26), "Upload-Speed: ", font=font, fill=255)
            draw.text((50,36), fbspeed[0], font=font, fill=255)
            draw.text((0,46), "Download-Speed: ", font=font, fill=255)
            draw.text((50,56), fbspeed[1], font=font, fill=255)
            disp2.display(image)

        elif elapsed_seconds >= 15 and elapsed_seconds <= 17:
            regulator = framerate_regulator(fps=10)
            left_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
            'res', 'Fallin-L.gif'))
            left = Image.open(left_path)
            size = [min(*disp.size)] * 2
            posn = ((disp.width - size[0]), disp.height - size[1])
            timecheck = time.time()
            
            while time.time() <= timecheck + giftimer:
                 for frame in ImageSequence.Iterator(left):
                    with regulator:
                        background = Image.new("RGB", disp.size, "white")
                        background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                        disp.display(background.convert("1"))
                    if time.time() >= timecheck + giftimer:
                       break
            
            regulator2 = framerate_regulator(fps=10)
            right_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
            'res', 'Fallin-R.gif'))
            right = Image.open(right_path)
            size = [disp.size]
            posn = ((disp.width - size[0]), disp.height - size[1])
            timecheck = time.time()
            
            while time.time() <= timecheck + giftimer:
                 for frame in ImageSequence.Iterator(right):
                    with regulator2:
                        background = Image.new("RGB", disp.size, "white")
                        background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                        disp2.display(background.convert("1"))
                    if time.time() >= timecheck + giftimer:
                       break
                    
        else:
            try:
                req = requests.get('http://pi.hole/admin/api.php')
                data = req.json()
                draw.text((0, 0), "Pi-hole (%s)" % data["status"], font=font, fill=255)
                draw.line((0, 12, width, 12), fill=255)
                draw.text((0, 22), "Blocked: %d (%d%%)" % (data["ads_blocked_today"], data["ads_percentage_today"]), font=font, fill=255)                
                draw.text((0, 32), "Queries: %d" % data["dns_queries_today"], font=font, fill=255)
                draw.line((0, 50, width, 50), fill=255)
                draw.text((0, 54), "Blocklist: %d" % data["domains_being_blocked"], font=font, fill=255)                
            except:  ## noqa
                draw.text((0, 0), "ERROR!", font=font, fill=255)
                disp.display(image)
        
        time.sleep(sleep)

        elapsed_seconds += 1
except (KeyboardInterrupt, SystemExit):
    print("Exiting...")
