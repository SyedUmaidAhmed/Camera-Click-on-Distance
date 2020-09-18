from picamera.array import PiRGBArray
from picamera import PiCamera
from queue import Queue
import RPi.GPIO as GPIO                    #Import GPIO library                                #Import time library
GPIO.setmode(GPIO.BCM)
import threading
from threading import Thread
import time
import cv2
from datetime import datetime
from time import sleep
TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)       
global i
i = 0
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(320, 240))

        
while True:
    

    GPIO.output(TRIG, False)
    time.sleep(2)
    
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 0)
       

#    if distance > 2 and distance < 400:
    print ("Distance:",distance,"cm")
    i+=1
    if distance > 40:
        camera.capture("/home/pi/" + str(i) + ".jpg")
        


    else:
        print("Out Of Range")    
    

