import RPi.GPIO as GPIO
import time
import asyncio
 
class GPIOControl:
 
  def __init__(self):
    print("setting up the gpio board")
    GPIO.setmode(GPIO.BCM)
    chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
    GPIO.setup (chan_list, GPIO.OUT)
    GPIO.output (chan_list, GPIO.HIGH)
 
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
                 
  async def rotate_left (self, wait):
    print("GPIOControl: rotate_left")
    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
    await asyncio.sleep(wait)
    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  async def rotate_right (self, wait):
    print("GPIOControl: rotate_right")
    GPIO.output ([27, 5, 22], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
    await asyncio.sleep(wait)
    GPIO.output ([27, 5, 22], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
                 
  async def rotate_left_az (self, azimuth, info):
    print("GPIOControl: rotate_left_az")
    targ_az = int(azimuth) + 2
    got_there = False
    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH)) # start rotation
    while (not got_there):
      await asyncio.sleep(.1)
      curr_az = int(info.getInf("ADAZ"))
      if(curr_az==targ_az or curr_az==(targ_az-1) or curr_az==(targ_az+1)):
        got_there = True

    GPIO.output ([27, 5, 17], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)) # end rotation
                 
  async def rotate_right_az (self, azimuth, info):
    print("GPIOControl: rotate_right_az")
    targ_az = int(azimuth) - 2
    got_there = False
    GPIO.output ([27, 5, 22], (GPIO.LOW, GPIO.HIGH, GPIO.LOW)) # rotate
    while (not got_there):
      await asyncio.sleep(.1)
      curr_az = int(info.getInf("ADAZ"))
      if(curr_az==targ_az or curr_az==(targ_az-1) or curr_az==(targ_az+1)):
        got_there = True
    GPIO.output ([27, 5, 22], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)) # end rotation
