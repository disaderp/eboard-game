#!/usr/bin/python
# -*- coding:utf-8 -*-
import cam
import display
from tracks import Track 
import os
import time
from PIL import Image,ImageDraw,ImageFont
picdir = "."

player1 = Track(7)
display.init()
display.insertBmp(Image.open(os.path.join(picdir, 'menu.bmp')), None)
display.writeText(15, 25, 'hello')
display.writeText(15, 45, cam.checkDice())
display.writeText(25, 350, 'A')
display.writeText(95, 350, 'B')
display.writeText(170, 350, 'C')
display.writeText(240, 350, 'D')
display.draw()
player1.activateField(8)
time.sleep(5)
display.clear()
display.stop()
player1.activateField(0)