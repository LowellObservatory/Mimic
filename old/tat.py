import asyncio
import serial_asyncio
import re
import time
from GPIOControl import GPIOControl

async def main(loop):
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB0', baudrate=9600)
  cont = GPIOControl()

  print('Reader Created')

  recTick = recvTick(tickReader)
  kTick = recvK(cont)

  await asyncio.wait([recTick, kTick])

async def recvTick(r):
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.strip().decode('ascii')
    print(msg.strip())
    print(msgascii)

async def recvK(cont):
  print("hello")
  await cont.rotate_left(10)
  await asyncio.sleep(5)
  await cont.rotate_right(10)
  return("ktick")

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
