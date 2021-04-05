import serial
import re
import time
from InfPacket import InfPacket



def recv(ser):
  while(True):
      msg = ser.read(4)
      msgascii = msg.decode('ascii')
      print("message received: " + msgascii)


if __name__ == '__main__':
  ser = serial.Serial("/dev/ttyUSB0")
  print("connected to /dev/ttyUSB0")
  recv(ser)
