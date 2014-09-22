Pystromo
========

Current Version: 0.6.1
----------------------

### Introduction

I'm being lazy and just copying helpful text from around the web to this readme.  Attribution where possible. (This README originaly compiled by https://github.com/bryongibson)

### Project Home

Website:    https://launchpad.net/pystromo

Author:     https://launchpad.net/~raumkraut (Muchos gracias!!!)

*A Python program which allows arbitrary remapping of input events from any standard linux input device. It can turn any input device into virtually any other; joysticks controlling the mouse pointer, mice pretending to be keyboards, keyboards masquerading as joysticks!*

*Though originally only targetted at improving linux support for the Belkin Nostromo n52 with arbitrary macros, once I had finished researching how it would be implemented, expanding it's scope to cover any USB device was trivial. Theoretically non-USB devices could also be supported, but that has yet to be tested.*

*Pystromo currently consists of two daemons/scripts; pystromo-remap.py, which performs the remapping of input; and pystromo-monitor.py, whose role is to automatically start and stop the remapper in response to which applications are running.*

*As best as I can remember, and with the exception of graphical configuration tools, Pystromo now matches and exceeds all the functionality of the Windows Nostromo driver software.*    -- Raumkraut

### Installation

I.  http://www.thelupine.com/content/pystromo-and-belkin-n52te

Getting the Belkin Nostromo n52te working in Linux is pretty simple. You can use pystromo: https://launchpad.net/pystromo

For this, under Karmic, I simply needed to add uinput to my /etc/modules file (for reboot) and manually load it once for now:
sudo sh -c "echo uinput >> /etc/modules"
sudo modprobe uinput

Then, after extracting the pystromo-0.6.0.tar.gz file, I just copied the pystromo/config/52-pystromo-debian.rules file into /etc/udev/rules.d/52-pystromo-debian.rules
tar -xvf pystromo-0.6.0.tar.gz
sudo cp pystromo/config/52-pystromo-debian.rules /etc/udev/rules.d/52-pystromo-debian.rules

Next, I reloaded the udev rules:
sudo udevadm control --reload-rules
sudo udevadm trigger

Then, I moved the extracted pystromo folder into my ~/.config directory
mv pystromo ~/.config/

Finally, I just made sure to add an auto-launcher for:

python ~/.config/pystromo/pystromo-mon.py 

...and everything is good to go.  This will make sure pystromo is up and running each time your reboot.  Otherwise, if you want to run it manually each time, then just type the above into a "run" dialog.

II.  http://ubuntuforums.org/showthread.php?t=948833

### Troubleshooting

https://answers.launchpad.net/pystromo
