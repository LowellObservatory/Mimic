import asyncio
import serial_asyncio
import re
import time
from InfPacket import InfPacket
from DrvCommands import DrvCommands
import DomeControl

async def main(loop):
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB0', baudrate=9600)
  driverReader, driverWriter = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB1', baudrate=9600)
  info = InfPacket()
  drvc = DrvCommands()

  print('Readers, Writer, Created')

  recTick = recvTick(tickReader, info, drvc)
  recComm = recvComm(driverReader, driverWriter, info, drvc)

  await asyncio.wait([recTick, recComm])

async def recvTick(r, info, drvc):
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.strip().decode('ascii')
    print("recvTick: " + msgascii)
    info.setInf("ADAZ", int(msgascii))

async def recvComm(r, w, info, drvc):
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.decode('ascii')
    print("recvComm: message received: " + msgascii)
    await drvc.command_to_function(msgascii, w, info)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
