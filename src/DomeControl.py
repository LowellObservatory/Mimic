import time
import GPIOControl as ctl
 
class DomeControl:
 
  def __init__(self):
    # Initialize Dome Status
 
  def go_home (wait):
  def close_shutter (wait):
 
  def open_shutter (Dome.State, wait):
    ctl.upper_shutter_open(Dome.State, wait)
    ctl.lower_shutter_open (Dome.State, wait)
  
  def goto_azimuth (azimuth):
    leftRight = calculate_direction(Dome.State)
    timeToMove = calculate_move_time(Dome.State)
    if (timeToMove > 1.0)):          # seconds
      if (leftRight == 'left'):
        ctl.rotate_left(timeToMove)
      else
        ctl.rotate_right(timeToMove)
