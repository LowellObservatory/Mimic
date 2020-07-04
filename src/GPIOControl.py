import RPi.GPIO as GPIO
import time
 
class GPIOControl:
 
  def __init__(self, domestate):
    GPIO.setmode (GPIO.BOARD)
    chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
    GPIO.setup (chan_list, GPIO.OUT)
    GPIO.output (chan_list, GPIO.HIGH)
    self.domestate = domestate
 
  def upper_shutter_open (wait):
    GPIO.output ([26, 23, 24], (GPIO_HIGH, GPIO_LOW, GPIO_HIGH))
    time.sleep(wait)
    GPIO.output ([26, 23, 24], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.Upper_Shutter = "open"
 
  def upper_shutter_close (wait):
    GPIO.output ([26, 23, 24], (GPIO_LOW, GPIO_HIGH, GPIO_LOW))
    time.sleep(wait)
    GPIO.output ([26, 23, 24], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.Upper_Shutter = "closed"
                 
  def lower_shutter_open (wait):
    GPIO.output ([6, 25, 16], (GPIO_HIGH, GPIO_LOW, GPIO_HIGH))
    time.sleep(wait)
    GPIO.output ([6, 25, 16], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.Lower_Shutter = "open"
                 
  def lower_shutter_close (wait):
    GPIO.output ([6, 25, 16], (GPIO_LOW, GPIO_HIGH, GPIO_LOW))
    time.sleep(wait)
    GPIO.output ([6, 25, 16], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.Lower_Shutter = "closed"
                 
  def rotate_left (wait):
    self.domestate.isMoving = "True"
    GPIO.output ([27, 5, 17], (GPIO_HIGH, GPIO_LOW, GPIO_HIGH))
    time.sleep(wait)
    GPIO.output ([27, 5, 17], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.isMoving = "False"
                 
  def rotate_right (wait):
    self.domestate.isMoving = "True"
    GPIO.output ([27, 5, 17], (GPIO_LOW, GPIO_HIGH, GPIO_LOW))
    time.sleep(wait)
    GPIO.output ([27, 5, 17], (GPIO_HIGH, GPIO_HIGH, GPIO_HIGH))
    self.domestate.isMoving = "False"
 
