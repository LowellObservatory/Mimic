import time
import asyncio
from GPIOControl import GPIOControl
from setup_logger import logger

class DomeControl:

  def __init__(self):
    print("DomeControl init")
    self.gpioctl = GPIOControl()
 
  def abort (self, info):
    print("got abort command in DomeControl")
    self.gpioctl.abort(info)

  async def go_home (self, info):
    print("DomeControl: go_home")
    await self.goto_azimuth(58, info)
    
  def close_shutter (self, info):
    print("DomeControl: close_shutter")
    self.gpioctl.lower_shutter_close (100)
    self.gpioctl.upper_shutter_close(140)
    info.setInf("Shutter", 1)
 
  def open_shutter (self, info):
    print("DomeControl: open_shutter")
    self.gpioctl.upper_shutter_open(140)
    self.gpioctl.lower_shutter_open (100)
    info.setInf("Shutter", 2)
  
  async def goto_azimuth (self, azimuth, info):
    print("DomeControl: goto_azimuth: " + str(azimuth)) 
    curr_az = (info.getInf("ADAZ") - info.getInf("DOMEOFF")) % 360
    print("curr_az: " + str(curr_az))
    print("azimuth_target: " + str(azimuth))

    # Figure out how far to turn and direction.
    print(type(curr_az))
    print(type(azimuth))
    intaz = int(azimuth)
    az_to_go = abs(curr_az - intaz)
    if (az_to_go > 180):
      az_to_go = 360 - az_to_go
      right = intaz < curr_az
    else:
      right = intaz > curr_az

    print("az_to_go: " + str(az_to_go))
    print("right: " + str(right))
    
    if (az_to_go < 1):
      return

    # Calculate time to move
#    t = 110.0/360.0 * (az_to_go - 1.5)
#    t = int(round(t))
#    print("time: " + str(t))
#    if (t <= 0):
#      return

    # Go, ADAZ will update automatically as the dome turns.
    if (az_to_go == 1):
      print("nudging one degree")
      if (right):
        logger.debug('nudge one degree right')
        await self.gpioctl.rotate_right(0.15)
      else:
        logger.debug('nudge one degree left')
        await self.gpioctl.rotate_left(0.15)
    elif (az_to_go == 2):
      print("nudging two degrees")
      if (right):
        logger.debug('nudge two degrees right')
        await self.gpioctl.rotate_right(0.3)
      else:
        logger.debug('nudge two degrees left')
        await self.gpioctl.rotate_left(0.3)
    else:
      if (right):
        logger.debug('rotate right az')
        await self.gpioctl.rotate_right_az(azimuth, info)
      else:
        logger.debug('rotate left az')
        await self.gpioctl.rotate_left_az(azimuth, info)
      return
