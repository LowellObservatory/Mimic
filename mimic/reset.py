import time
import asyncio

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, GPIO.HIGH)
