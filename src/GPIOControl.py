import RPi.GPIO as GPIO
import time
 
class GPIOControl:
 
  def __init__(self):
    GPIO.setmode (GPIO.BOARD)
    chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
    GPIO.setup (chan_list, GPIO.OUT)
    GPIO.output (chan_list, GPIO.HIGH)
 
  def upper_shutter_open (wait)
    GPIO.output ([26, 23, 24], (GPIO_HIGH, GPIO_LOW, GPIO_HIGH)
    time.sleep(wait)
    GPIO.output ([26, 23, 24], (GPIO_HIGH, GPIO.HIGH, GPIO_HIGH)
    Dome.State.Upper_Shutter = "open"
 
  def upper_shutter_close (wait):
  def lower_shutter_open (wait):
  def lower_shutter_close (wait):
  def rotate_left (wait):
  def rotate_right (wait):
 
