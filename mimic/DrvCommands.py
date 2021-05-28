# Respond to Command, the command routines are async so we can use await, etc.

# imports
import re
import time
import asyncio

from .DomeControl import DomeControl
from .setup_logger import logger


class DrvCommands:
    def __init__(self):
        self.dmctl = DomeControl()

    async def go_home(self, info):
        print("going home! DrvCommands: go_home")
        await self.dmctl.go_home(info)

    async def open_shutter(self, info):
        print("DrvCommands: open_shutter")
        curr_az = info.getInf("ADAZ")
        if curr_az < 63 or curr_az > 68:
            await self.dmctl.go_home(info)
            time.sleep(5)
        self.dmctl.open_shutter(info)

    async def close_shutter(self, info):
        print("DrvCommands: close_shutter")
        curr_az = info.getInf("ADAZ")
        if curr_az < 63 or curr_az > 68:
            await self.dmctl.go_home(info)
            time.sleep(5)
        self.dmctl.close_shutter(info)

    async def set_azimuth(self, az, info):
        print("DrvCommands: set_azimuth: " + str(az))
        await self.dmctl.goto_azimuth(az, info)

    async def send_inf(self, writer, info):
        print("DrvCommands: send_inf")
        inf_pack = info.getInfPack()
        print(inf_pack)
        writer.write(inf_pack)
        print("Sent " + str(inf_pack))

    async def command_to_function(self, cmd, writer, info):
        # cmd - command received from driver
        # writer - asyncronous serial writer to send byte strings to ASCOM
        # info - an instance of the InfPacket class we use as a data struct

        # if we see a G followed by three numbers, ie. G123 it
        # means move dome to azimuth "123"

        # print("DrvCommands: command_to_function: " + cmd )
        logger.debug("DrvCommands: " + cmd)

        # The preceeding 'r' treats \d as a string literal, which is what
        #   is wanted with a regular expression
        validGoString = r"G\d{3}"
        p = re.compile(validGoString)
        if p.match(cmd):
            print("calling goto_azimuth: " + str(cmd[1:4]))
            await self.dmctl.goto_azimuth(cmd[1:4], info)
        elif cmd == "GINF":  # request for info packet
            print("command_to_function: sending inf")
            await self.send_inf(writer, info)
        elif cmd == "GHOM":  # request to send the dome home
            await self.go_home(info)
        elif cmd == "GOPN":  # request to open the dome shutters
            await self.open_shutter(info)
        elif cmd == "GCLS":  # request to close the dome shutters
            await self.close_shutter(info)
        elif "ST" in cmd:  # abort
            self.dmctl.abort(info)

        await self.send_inf(writer, info)
