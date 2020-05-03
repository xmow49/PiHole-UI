# pihole-oled (for Raspberry Pi Zero)
---
This is a fork from: [pihole-oled](https://github.com/willdurand/pihole-oled)

I faced installation-problems with the original code, so I forked it, and changed the code.

#### What is "new" in this code?

- skipped addafruit module -> use "luma.oled"

#### To-Do / Plans for new Features:

- Integrate [Fritzconnection](https://pypi.org/project/fritzconnection/)
- Maybe change the UI -> Grafics? Animations?


## Hardware
---

The OLED display is connected _via_ I2C with 4 wires: `SDA`, `SCL`, `3.3V` and
`GND`.

## Information:
---

This project requires:
- a Raspberry Pi Zero (or 3/4 with wifi -> "wlan0" is used in the code, not "eth0")
- An 0.96" Oled (ssd1306) with i2c
- Raspbian Buster Lite Image

## Make an SD-Card with an "Raspbian Buster Lite" Image ready:
---

#### 1st - Download Raspbian Buster LITE Image:

[Raspbian Images](https://www.raspberrypi.org/downloads/raspbian/)

#### 2nd - flash it to the SD-Card:

Use "Win32Diskimager"

#### 3rd - Go to the "root" folder of the SD Card

- Open "config.txt"
  -> remove the "#" before "dtparam=spi=on" to activate SPI

- make a new textfile called "ssh" -> no .txt at the end!

- Make a new textfile called "wpa_supplicant.conf"
  -> put this text in it, and edit it for your case:
```  
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```
#### 4th - remove SD Card 

put SD-Card in your Pi Zero and let it boot (takes a few minutes)

#### 5th - Connect to the Pi Zero with SSH

Use Putty/Kitty (User: pi / PW: raspberry)



## 1st: Configure your PiZero:
---

```
sudo apt-get update

sudo dpkg-reconfigure tzdata
```
-> Select your Timezone

```
sudo raspi-config
```
-> 5 Interfacing Options -> P5 I2C -> enable i2c



## 2nd: Install PiHole
---

```
curl -sSL https://install.pi-hole.net | bash
```
-> follow the setup...
-> note the password in the last step!



## 3rd: Install the dependencies:
---

```
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio python3-rpi.gpio libopenjp2-7 libopenjp2-7-dev libtiff5 libcurl4-openssl-dev libssl-dev git 

sudo pip3 install -U pip

sudo pip3 install -U setuptools

sudo pip3 install humanize

sudo pip3 install psutil

sudo pip3 install luma.oled
```


## 4th: Install pihole-oled
---

```
git clone https://github.com/Maschine2501/pihole-oled.git /home/pi/pihole-oled

cd pihole-oled

sudo cp pihole-oled.service /etc/systemd/user/

sudo systemctl enable /etc/systemd/user/pihole-oled.service

sudo systemctl start pihole-oled.service

sudo reboot
```


## Nightly Build installation:
---

follow the installation steps above, until you finished step 3.

After Step 3 continue with this:

```
sudo pip3 install fritzconnection

git clone https://github.com/Maschine2501/pihole-oled.git /home/pi/pihole-oled

cd pihole-oled

sudo cp pihole-nightly.service /etc/systemd/user/

sudo systemctl enable /etc/systemd/user/pihole-nightly.service

sudo systemctl start pihole-nightly.service

sudo reboot
```


## If something is wrong:
---

### check the journal!

#### stable:
```
sudo journalctl -fu pihole-oled.service
```

#### nightly:
```
sudo journalctl -fu pihole-nightly.service
```




