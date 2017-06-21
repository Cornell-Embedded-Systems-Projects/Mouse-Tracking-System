# Mouse-Tracking-System

## Parts

Note that prices are subject to change, and can potentially be found cheaper elsewhere on the internet. These are simply example prices from reliable suppliers.

| Part Name | Reference Link | Price* |
 | --- | --- | --- |
 | Raspberry Pi 3 | https://www.raspberrypi.org/products/raspberry-pi-3-model-b/ | $39.95 from Adafruit Industries |
 | 5V Power Supply | https://www.adafruit.com/product/1995 | $7.50 from Adafruit Industries |
 | 8 Gb microSD card | https://www.adafruit.com/product/2692 | $9.95 from Adafruit Industries |
 | PiFace Shim RTC | http://www.piface.org.uk/products/piface_clock/ | $9.42 from element14 |
 
*Price as of 6/20/2017

## Guide

This guide assumes a working knowledge of how to use the Raspberry Pi. First, set up your Pi with your preffered Raspbian distribution (we used the one with desktop GUI to ease troubleshooting). Then, set up the PiFace RTC, using the most recent instructions from their Github repository: https://github.com/piface/PiFace-Real-Time-Clock For help verifying your clock's functionality, use the hwclock command (stands for hardware clock) in the Pi's terminal. Root permissions are required to use the command. For help, simply run `sudo hwclock --help`

