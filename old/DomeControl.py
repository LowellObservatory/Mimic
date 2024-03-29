import time
import asyncio
from GPIOControl import GPIOControl

class DomeControl:

  def __init__(self):
    print("DomeControl init")
    self.gpioctl = GPIOControl()
 
  async def go_home (self, info):
    print("DomeControl: go_home")
    await self.goto_azimuth(64, info)
    
  def close_shutter (self, info):
    print("DomeControl: close_shutter")
    self.gpioctl.lower_shutter_close (60)
    self.gpioctl.upper_shutter_close(100)
    info.setInf("Shutter", 1)
 
  def open_shutter (self, info):
    print("DomeControl: open_shutter")
    self.gpioctl.upper_shutter_open(100)
    self.gpioctl.lower_shutter_open (60)
    info.setInf("Shutter", 2)
  
  async def goto_azimuth (self, azimuth, info):
    print("DomeControl: goto_azimuth: " + str(azimuth)) 
    curr_az = info.getInf("ADAZ")
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
    
    if (az_to_go < 2):
      return

    # Calculate time to move
#    t = 110.0/360.0 * (az_to_go - 1.5)
#    t = int(round(t))
#    print("time: " + str(t))
#    if (t <= 0):
#      return

    # Go, ADAZ will update automatically as the dome turns.
    if (right):
      await self.gpioctl.rotate_right_az(azimuth, info)
    else:
      await self.gpioctl.rotate_left_az(azimuth, info)
    return
