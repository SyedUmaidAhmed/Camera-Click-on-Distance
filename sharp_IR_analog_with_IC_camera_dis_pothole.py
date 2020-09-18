
# ADD MODULES
# ---------------------------------------------------------
from picamera.array import PiRGBArray
from picamera import PiCamera
from queue import Queue
import threading
from threading import Thread
import time
import cv2
from datetime import datetime
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime
import RPi.GPIO as GPIO

# ---------------------------------------------------------
# GPIO CONFIGURATION
# ---------------------------------------------------------
global i
i = 0
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(320, 240))

GPIO.setmode(GPIO.BCM)

CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# ---------------------------------------------------------
# SHARP Infrared Sensor 10cm to 150cm CONFIGURATION
# ---------------------------------------------------------
def distance():
    runningTotal = 0
    avgFactor = 30
    for x in range(avgFactor):
        v = (mcp.read_adc(0) / 1023.0) * 3.3
        distance1 = (16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439)
        runningTotal = runningTotal + distance1
    else:
        distance = (runningTotal / avgFactor)

    return distance

# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------
if __name__ ==     '__main__':
    try:
        while True:
            dist = distance()
            d = int(dist)
            print("Distance {:.2f}".format(dist))
            i+=1
            if d > 40:
                camera.capture("/home/pi/approach/" + str(i) + ".jpg")

            
            time.sleep(1)

    except KeyboardInterrupt:
        print("Ending Script Coding")

