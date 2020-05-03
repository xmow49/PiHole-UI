# pihole-oled (for Raspberry Pi Zero)
---
This is a fork from: [pihole-oled]()

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
-> Select your Timezone

sudo raspi-config
-> 5 Interfacing Options -> P5 I2C -> enable i2c

```

### 2nd: Install PiHole
---

```
curl -sSL https://install.pi-hole.net | bash
```
-> follow the setup...
-> note the password in the last step!

### 3rd: Install the dependencies:
---

```
sudo apt-get install python3-pip

sudo pip3 install -U pip

sudo pip3 install -U setuptools

sudo pip3 install humanize

sudo pip3 install psutil

sudo pip3 install luma.oled



```


### Software requirements

If you do not have `pip3` installed, start by installing it:

```
sudo apt-get install python3-pip
```

If you do not have `pipenv` installed, install it too:

```
pip3 install --user pipenv
```

Note: the command above keeps everything into a `~/.local` directory. You can
update the current user's `PATH` by adding the following lines into your
`.bashrc` (or equivalent):

```
export PY_USER_BIN="$(python -c 'import site; print(site.USER_BASE + "/bin")')"
export PATH="$PY_USER_BIN:$PATH"
```

Now install a few libraries for
[Pillow](https://pillow.readthedocs.io/en/stable/index.html):

```
sudo apt-get install libopenjp2-7 libtiff5
```

### Project installation

Clone this project:

```
git clone https://github.com/Maschine2501/pihole-oled.git /home/pi/pihole-oled
```

Install the python dependencies:

```
cd /home/pi/pihole-oled
pipenv install
```

If you plug the OLED display and run the command below, you should see some
information on the display:

```
pipenv run python3 main.py
```

You can exit the script with <kbd>ctrl</kbd>+<kbd>c</kbd>.




### Systemd configuration

You can install a `systemd` service by copying the provided configuration file
using the command below. This service will automatically run the python script
mentioned in the previous section on boot:

```
sudo cp pihole-oled.service /etc/systemd/user/
```

Enable, then start the `pihole-oled.service`:

```
sudo systemctl enable /etc/systemd/user/pihole-oled.service
sudo systemctl start pihole-oled.service
```

## If something is wrong:
---

### check the journal!
```
sudo journalctl -fu rc2ui.service
```

