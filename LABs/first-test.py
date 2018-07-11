#!/usr/bin/env python

import RPi.GPIO as X
import time

X.setmode(X.BCM)
Relaypin = 4 # as BCM == Pin 7
X.setup(Relaypin, X.OUT)
i=5
while (i>0):
    X.output(Relaypin, X.LOW)
    time.sleep(1)
    X.output(Relaypin, X.HIGH)
    time.sleep(1)
    i=i-1
X.cleanup()
