import serial
import re
import time
import asyncio
from InfPacket import InfPacket
from DrvCommands import DrvCommands
from DomeControl import DomeControl
from GPIOControl import GPIOControl
import serial_asyncio
import re
import time

async def main(loop):
  gpio = GPIOControl()
  reck = test(gpio, 300)
  await asyncio.wait([reck])

async def test(gpio, wait):
  await gpio.rotate_right(wait)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()


