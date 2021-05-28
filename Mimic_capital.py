import asyncio
import serial_asyncio

from mimic.setup_logger import logger
from mimic.InfPacket import InfPacket
from mimic.DrvCommands import DrvCommands


async def main(loop):
    # Connect to the bar code reader.
    tickReader, _ = await serial_asyncio.open_serial_connection(
        url="/dev/domeaz", baudrate=9600
    )
    # Connect to the nuc.
    driverReader, driverWriter = await serial_asyncio.open_serial_connection(
        url="/dev/nuc", baudrate=9600
    )
    info = InfPacket()
    drvc = DrvCommands()

    print("Readers, Writer, Created")

    recTick = recvTick(tickReader, info, drvc)
    recComm = recvComm(driverReader, driverWriter, info, drvc)

    await asyncio.wait([recTick, recComm])


async def recvTick(r, info, drvc):
    checking = ""
    charCount = 0
    msg = ""
    while True:
        oneByte = await r.readexactly(1)
        checking = oneByte.decode("ascii")
        #    print("recvTick: " + checking)
        if checking != "\r":
            msg = msg + checking
            charCount = charCount + 1
        else:
            msg = ""
            charCount = 0

        if charCount == 3:
            #      print("recvTick: " + msg)
            logger.debug("recvTick: " + msg)
            string = "abcd"
            try:
                info.setInf("ADAZ", int(msg))
            except ValueError:
                logger.debug("recvTick: Bad Azimuth")
            msg = ""
            charCount = 0


async def recvComm(r, w, info, drvc):
    while True:
        msg = await r.readexactly(4)
        print(msg)
        msgascii = msg.decode("ascii")
        if "ST" in msgascii:  # The STOP command has a "\n" after it
            msg = await r.readexactly(1)  # Skip this character.
        print("recvComm: message received: " + msgascii)
        await drvc.command_to_function(msgascii, w, info)


if __name__ == "__main__":
    # TODO :
    #   - Split common config parameters out to a conf file (home, timing, etc)
    #   - Stub in LED stuff
    #   - Add in broker advertising and formatting
    #   - Set up logger(s) uniformly and pass them around
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
