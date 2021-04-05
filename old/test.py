import serial
import re
import time
from InfPacket import InfPacket


def recv(info, ser):
  p = re.compile('G\d{3}')
  while(True):
      msg = ser.read(4)
      msgascii = msg.decode('ascii')

      print("message received: " + msgascii)
      if (msgascii == "GINF"):
        infpacket = info.getInfPack()
        print("message sent: " + infpacket.decode('ascii'))
        ser.write(infpacket)
      elif (p.match(msgascii)):
        print("setting ADAZ")
        info.setInf("ADAZ",int(msgascii[1:4]))
        print("waiting 3 seconds")
        time.sleep(3)
        infpacket = info.getInfPack()
        print("message sent: " + infpacket.decode('ascii'))
        ser.write(infpacket)


if __name__ == '__main__':
  info = InfPacket()
  ser = serial.Serial("/dev/ttyUSB1")
  print("connected to /dev/ttyUSB1")
  recv(info, ser)
