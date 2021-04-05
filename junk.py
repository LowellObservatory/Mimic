import re
import time
import RPi.GPIO as GPIO
 
class GPIOControl:
 
  def __init__(self):
    print("setting up the gpio board")
    GPIO.setmode(GPIO.BCM)
    self.chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
    GPIO.setup (self.chan_list, GPIO.OUT)
    GPIO.output (self.chan_list, GPIO.HIGH)
 
  def abort (self, info):
    print("abort in GPIO")
    GPIO.output (self.chan_list, GPIO.HIGH)

#    print("666")
#    info.setInf("ABORT", 666)

  def upper_shutter_open (self, wait):
    print("GPIOControl: upper_shutter_open")
    GPIO.output ([26, 23, 24], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
    time.sleep(wait)
    GPIO.output ([26, 23, 24], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
 
  def upper_shutter_close (self, wait):
    print("GPIOControl: upper_shutter_close")
    GPIO.output ([26, 23, 24], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
    time.sleep(wait)
    GPIO.output ([26, 23, 24], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  def lower_shutter_open (self, wait):
    print("GPIOControl: lower_shutter_open")
    GPIO.output ([6, 25, 16], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
    time.sleep(wait)
    GPIO.output ([6, 25, 16], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  def lower_shutter_close (self, wait):
    print("GPIOControl: lower_shutter_close")
    GPIO.output ([6, 25, 16], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
    time.sleep(wait)
    GPIO.output ([6, 25, 16], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  def rotate_left (self, wait):
    print("GPIOControl: rotate_left")
    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
    time.sleep(wait)
    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  def rotate_right (self, wait):
    print("GPIOControl: rotate_right")
    GPIO.output ([27, 5, 22], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
    time.sleep(wait)
    GPIO.output ([27, 5, 22], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 

gpio = GPIOControl()
gpio.rotate_right(5)
