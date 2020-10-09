import asyncio
import serial_asyncio
import re
import time
from InfPacket import InfPacket
from DrvCommands import DrvCommands
import DomeControl

async def main(loop):
  # Connect to the bar code reader.
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/domeaz', baudrate=9600)
  # Connect to the nuc.
  driverReader, driverWriter = await serial_asyncio.open_serial_connection(
    url='/dev/nuc', baudrate=9600)
  info = InfPacket()
  drvc = DrvCommands()

  print('Readers, Writer, Created')

  recTick = recvTick(tickReader, info, drvc)
  recComm = recvComm(driverReader, driverWriter, info, drvc)

  await asyncio.wait([recTick, recComm])

async def recvTick(r, info, drvc):
  oneatatime = True
  checking = " "
  # We read one character at a time until we find a newline character.
  # Once a newline character is found, begin reading four characters at once.
  while True:
    if (oneatatime):
      while (checking != "\r"):
        msg = await r.readexactly(1)
        print(msg)
        checking = msg.decode('ascii')
        print("checking: " + checking)
      oneatatime = False
    else:
      msg = await r.readexactly(4)
      msgascii = msg.strip().decode('ascii')
#      print("recvTick: " + msgascii)
      info.setInf("ADAZ", int(msgascii))

async def recvComm(r, w, info, drvc):
  while True:
    msg = await r.readexactly(4)
    print(msg)
    msgascii = msg.decode('ascii')
    if ("ST" in msgascii):         # The STOP command has a "\n" after it
      msg = await r.readexactly(1) # Skip this character.
    print("recvComm: message received: " + msgascii)
    await drvc.command_to_function(msgascii, w, info)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
