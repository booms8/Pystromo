Pystromo
========

Current Version: 0.6.0
----------------------

### Introduction

I'm being lazy and just copying helpful text from around the web to this readme.  Attribution where possible.

### Project Home

Website:    https://launchpad.net/pystromo

Author:     https://launchpad.net/~raumkraut (Muchos gracias!!!)

A Python program which allows arbitrary remapping of input events from any standard linux input device. It can turn any input device into virtually any other; joysticks controlling the mouse pointer, mice pretending to be keyboards, keyboards masquerading as joysticks!

Though originally only targetted at improving linux support for the Belkin Nostromo n52 with arbitrary macros, once I had finished researching how it would be implemented, expanding it's scope to cover any USB device was trivial. Theoretically non-USB devices could also be supported, but that has yet to be tested.

Pystromo currently consists of two daemons/scripts; pystromo-remap.py, which performs the remapping of input; and pystromo-monitor.py, whose role is to automatically start and stop the remapper in response to which applications are running.

As best as I can remember, and with the exception of graphical configuration tools, Pystromo now matches and exceeds all the functionality of the Windows Nostromo driver software.

### Installation

http://www.thelupine.com/content/pystromo-and-belkin-n52te

http://ubuntuforums.org/showthread.php?t=948833

### Troubleshooting

https://answers.launchpad.net/pystromo
