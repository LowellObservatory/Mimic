import serial
import re
import time
import asyncio
from InfPacket import InfPacket
from DrvCommands import DrvCommands
from DomeControl import DomeControl
import serial_asyncio
import re
import time

async def main(loop):
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB0', baudrate=9600)
  driverReader, driverWriter = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB1', baudrate=9600)
  info = InfPacket()
  drvc = DrvCommands()
  dctl = DomeControl()
  reck = test(drvc, driverWriter,  info)
  await asyncio.wait([reck])

async def test(drvc, w,  info):
  await drvc.command_to_function("GHOM", w, info)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()


