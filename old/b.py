import asyncio
import serial_asyncio
import re
import time
from GPIOControl import GPIOControl

def recvK(cont):
  print("hello")
  cont.rotate_left(1)
  cont.rotate_right(1)
  return("ktick")

cont = GPIOControl()
xyz = recvK(cont)
print(xyz)
