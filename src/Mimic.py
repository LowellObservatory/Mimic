# Respond to Command, the command routines are async so we can use await, etc.

# imports
import DomeControl as dc

class Mimic:
 
 def __init__(self):
  domestate =	{
    "isHome": True,
    "isMoving": False,
    "Upper_Shutter": "closed",
    "Lower_Shutter": "closed",
    "Azimuth": 75,
    "FastTracMode": False,
    "slop": 1.5,
    "degreespersecond": 2.0
  }
 
async def GoHome():
  if (domestate.isHome):
    return
  await domestate.isMoving == False
  # Determine direction to move dome. (shortest distance to home)
  # Determine distance to be moved, calculate approximate time to move.
  # Command move GPIO pin on for calculated time. (minus one second)
  # Monitor movement by reading position from UART. (bar code reader)
  # When initial move is done, check position, move again if outside range.
 
async def OpenShutter():
  if (domestate.ShutterOpen):
    return
  await domestate.isMoving == False  # probably bad code but this is the idea
  if (!domestate.isHome):
    dc.go_home()
  dc.open_shutter(waittime)
  # Set domestate.Upper_Shutter to "open".
  # Set domestate.Lower_Shutter to "open".
   
async def CloseShutter():
  if (domestate.Upper_shutter == "closed" && domestate.Lower_Shutter == "closed"):
      return
  await domestate.isMoving == False  # probably bad code but this is the idea
  if (!domestate.isHome):
    dc.go_home()
  dc.close_shutter(waittime)
  # Set domestate.Upper_Shutter to "closed".
  # Set domestate.Lower_Shutter to "closed".
 
async def ToFastTrackMode():
  await domestate.isMoving == False  # probably bad code but this is the idea
  domestate.FastTrackMode = True
 
async def SetAzimuth(az):
  await domestate.isMoving == False  # probably bad code but this is the idea
  lower = domestate.Azimuth - domedtate.slop
  upper = domestate.Azimuth + domestate.slop
  if (lower <= domestate.Azimuth <= upper):
    return
  # We will need to be careful with the above near zero azimuth.
  # Now calculate the difference between "az", the commanded azimuth
  #   and DomeState.Azimuth.  Calculate a direction and time based on this difference.
  # Turn the appropriate GPIO pin on for that time.
  # Check new position and update if not within slop limits.
  # We can read the barcode reader for the azimuth while moving because the wait
  #   time is done by "await asyncio.sleep(waitTime)", not time.sleep(waitTime).
 
def command_to_function(arg):
  # if we see a G followed by three numbers, ie. G123 it means move dome to azimuth "123"
  p = re.compile('G\d{3}'))
  if (p.match(arg)):
    dc.goto_azimuth(arg[1:3])
    return
 
  pseudocase = {
    GHOM : GoHome,
    GOPN : OpenShutter,
    GCLS : CloseShutter,
    GTCK : FastTrackMode
      # etc. etc. etc.
  }
 
  func = pseudocase.get(arg, lambda: "Invalid command")
  func()
