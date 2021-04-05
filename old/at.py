import asyncio
import serial_asyncio
import re
import time
from InfPacket import InfPacket
import DomeControl

async def main(loop):
  tickReader, _ = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB0', baudrate=9600)
  driverReader, driverWriter = await serial_asyncio.open_serial_connection(
    url='/dev/ttyUSB1', baudrate=9600)
  info = InfPacket()

  print('Reader Created')

  recTick = recvTick(tickReader, info)
  recComm = recvComm(driverReader, driverWriter, info)

  await asyncio.wait([recTick, recComm])

async def recvTick(r, info):
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.strip().decode('ascii')
    print(msg.strip())
    print(msgascii)

async def sendComm(w, msg):
  w.write(msg)
  print("sent " + msg.decode('ascii'))

async def recvComm(r, w, info):
  p = re.compile('G\d{3}')
  while True:
    msg = await r.readexactly(4)
    msgascii = msg.decode('ascii')
    print("message received: " + msgascii)
    if (msgascii == "GINF"):
      infpacket = info.getInfPack()
      print("message sent: " + infpacket.decode('ascii'))
      sent = sendComm(w, infpacket)
      await asyncio.wait([sent])
    elif (p.match(msgascii)):
      await DomeControl.goto_azimuth(int(msgascii[1:4]), info)
#      print("setting ADAZ")
#      info.setInf("ADAZ",int(msgascii[1:4]))
#      print("waiting 10 seconds")
#      await asyncio.sleep(10)
      infpacket = info.getInfPack()
      print("message sent: " + infpacket.decode('ascii'))
      sent = sendComm(w, infpacket)
      await asyncio.wait([sent])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
