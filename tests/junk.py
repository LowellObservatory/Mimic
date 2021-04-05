import asyncio
import serial_asyncio
import re
import time
from InfPacket import InfPacket
from DrvCommands import DrvCommands
import DomeControl

drvc = DrvCommands()
drvc.command_to_function("GINF", None, None)

