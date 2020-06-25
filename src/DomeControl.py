import time
import GPIOControl as ctl
 
class DomeControl:
 
  def __init__(self, domestate):
    # Initialize Dome Status
 
  def go_home (wait):
    self.goto_azimuth(domestate.Home_Position)
    
  def close_shutter (wait):
    ctl.upper_shutter_close(domestate, wait)
    ctl.lower_shutter_close (domestate, wait)
 
  def open_shutter (domestate, wait):
    ctl.upper_shutter_open(domestate, wait)
    ctl.lower_shutter_open (domestate, wait)
  
  def goto_azimuth (azimuth):
    leftRight = calculate_direction(domestate)
    timeToMove = calculate_move_time(domestate)
    if (timeToMove > 1.0)):          # seconds
      if (leftRight == 'left'):
        ctl.rotate_left(timeToMove)
      else
        ctl.rotate_right(timeToMove)
