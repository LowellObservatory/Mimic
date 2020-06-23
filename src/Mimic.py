# Respond to Command, the command routines are async so we can use await, etc.

# imports

class Mimic:
 
 def __init__(self):
  domestate =	{
    "isHome": True,
    "isMoving": False,
    "Shutter": "closed",
    "Azimuth": 75,
    "slop": 1.5,
    "degreespersecond": 2.0
  }
 
async def GoHome():
  if (DomeState.isHome):
    return
  await DomeState.Moving == False
  # Determine direction to move dome. (shortest distance to home)
  # Determine distance to be moved, calculate approximate time to move.
  # Command move GPIO pin on for calculated time. (minus one second)
  # Monitor movement by reading position from UART. (bar code reader)
  # When initial move is done, check position, move again if outside range.
 
async def OpenShutter():
  if (DomeState.ShutterOpen):
    return
  await DomeState.Moving == False  # probably bad code but this is the idea
  if (!DomeState.isHome):
    GoHome()
  # Command the shutter to open. (set GPIO pin high)
  # Wait prescribed time.
  # (set GPIO pin low)
  # Set DomeState.ShutterOpen to True, ShutterClosed to false.
   
async def CloseShutter():
  if (DomeState.ShutterClosed):
      return
  await DomeState.Moving == False  # probably bad code but this is the idea
  if (!DomeState.isHome):
    GoHome()
  # Similar to OpenShutter above.
 
async def ToFastTrackMode():
  await DomeState.Moving == False  # probably bad code but this is the idea
  DomeState.FastTrackMode = True
 
async def SetAzimuth(az):
  await DomeState.Moving == False  # probably bad code but this is the idea
  lower = DomeState.Azimuth - DomeState.slop
  upper = DomeState.Azimuth + DomeState.slop
  if (lower <= DomeState.Azimuth <= upper):
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
    SetAzimuth(arg[1:3])
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
