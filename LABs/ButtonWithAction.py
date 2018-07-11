#!/usr/bin/env python2.7  

import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)  

Buttonpin = 23 # BOARD == Pin 7  
Relaypin = 4 # as BCM == Pin 7
# GPIO 4 set up as input. It is pulled up to stop false signals  
GPIO.setup(Buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(Relaypin, GPIO.OUT)  
print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO port 4 (pin 7) to GND (pin 6)\n"  
while True:  
    print "Waiting for falling edge on port 4"  
    # now the program will do nothing until the signal on port 23   
    # starts to fall towards zero. This is why we used the pullup  
    # to keep the signal high and prevent a false interrupt  

    print "Press your button when ready to initiate a falling edge interrupt."  
    try:  
        GPIO.wait_for_edge(Buttonpin, GPIO.FALLING)  
        print "\nFalling edge detected. Now your program can continue with"  
        print "whatever was waiting for a button press."
        GPIO.output(Relaypin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(Relaypin, GPIO.HIGH)  
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  