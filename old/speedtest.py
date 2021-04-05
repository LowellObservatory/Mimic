import serial
import re
import time
import asyncio
import serial_asyncio
import GPIOControl as gpio

async def main(loop):
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB0', baudrate=9600)
  print('Reader Created')

  recTick = recvTick(tickReader)
  ti = dotest(10)

  await asyncio.wait([recTick])

async def recvTick(r):
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.strip().decode('ascii')
    print(msg.strip())
    print(msgascii)

#async def doTest(t):
#  gpio.start_rotate_right()
#  await asyncio.sleep(t)
#  gpio.stop_rotate_right()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
