#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pin_led = 12 
intensite = 1 

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin_led, GPIO.OUT) 
led = GPIO.PWM(pin_led,intensite) 

led.start(intensite) 

while intensite < 100:
        print('Intensite : {}'.format(intensite))
        led.ChangeFrequency(intensite) 
        time.sleep(2) 
        intensite += 10 
led.stop() 
GPIO.cleanup() 