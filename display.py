import sys
import os
import logging
import epaper
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

picdir = "."

epd = epaper.EPD()

blackBuffer = Image.new('1', (epd.height, epd.width), 255) #vertical
redBuffer = Image.new('1', (epd.height, epd.width), 255)

defFont = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

#logging.basicConfig(level=logging.INFO)

def insertBmp(imgBl, imgRe): #type Image
	if imgBl is not None:
		blackBuffer.paste(imgBl, (0,0))
	if imgRe is not None:
		redBuffer.paste(imgRe, (0,0))

def draw():
	epd.display(epd.getbuffer(blackBuffer), epd.getbuffer(redBuffer))

def writeText(x, y, text):
	drawblack = ImageDraw.Draw(blackBuffer)
	drawblack.text((x, y), text, font = defFont, fill = 0)

def init():
	epd.init()
	epd.Clear()

def newCanvas():
	blackBuffer = Image.new('1', (epd.height, epd.width), 255)
	redBuffer = Image.new('1', (epd.height, epd.width), 255)

def clear():
	epd.Clear()

def stop():
	epd.sleep()
