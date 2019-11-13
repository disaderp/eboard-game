# Modules

* Raspberry Pi 4
* [Waveshare E-Paper 4'2 B](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_(B))
* [Waveshare Camera NoIR H](https://www.waveshare.com/wiki/RPi_Camera_(H))
* 4 x [Waveshare MCP23017 Expansion Board](https://www.waveshare.com/wiki/MCP23017_IO_Expansion_Board)

# Installation

## Camera

Enable Camera interface
* raspi-config -> enable camera

## E-Paper

Enable SPI interface
* raspi-config -> enable SPI

Install BCM library
* wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
* tar zxvf bcm2835-1.60.tar.gz 
* cd bcm2835-1.60/
* ./configure
* make
* make check
* make install

Install WiringPI
* cd /tmp
* wget https://project-downloads.drogon.net/wiringpi-latest.deb
* sudo dpkg -i wiringpi-latest.deb

Install Python and SPI libraries
* apt-get update
* apt-get install python-pip
* apt-get install python-pil
* apt-get install python-numpy
* pip install RPi.GPIO
* pip install spidev

## MCP23017

Enable I2C interface
* raspi-config -> enable I2C

Install I2C tool
* apt-get install i2c-tools

## Other depedencies

OpenCV
* apt-get install python-opencv


