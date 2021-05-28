import collections


class InfPacket:
    def __init__(self):
        # We use an "ordered dictionary" from "collections" because the order
        # is important when we retreive an "info packet".
        self.domeinf = collections.OrderedDict()

        # Version String
        self.domeinf["Verstr"] = "V4"

        # Dome circumference in ticks.
        self.domeinf["Dticks"] = 360

        # Azimuth location of Home position in ticks.
        self.domeinf["Home1"] = 65

        # Coast value in ticks.
        self.domeinf["Coast"] = 2

        # Current Dome azimuth in ticks.
        self.domeinf["ADAZ"] = 65

        # Slave status, 0=off, 1=on.
        self.domeinf["Slave"] = 0

        # Shutter status, 0=unknown, 1=closed, 2=open.
        self.domeinf["Shutter"] = 1

        # Dome Support Ring status, 0=unk, 1=closed, 2=open.
        self.domeinf["DSR status"] = 1

        # Home sensor, 0 = home, 1 = not home.
        self.domeinf["Home"] = 0

        # Azimuth ticks of CCW edge of Home position.
        self.domeinf["HTICK_CCLK"] = 63

        # Azimuth ticks of CW edge of Home position.
        self.domeinf["HTICK_CLK"] = 67

        # Status of all user digital output pins.
        self.domeinf["UPINS"] = 0

        # Age of weather info.
        self.domeinf["WEAAGE"] = 128

        # Wind direction.
        self.domeinf["WINDDIR"] = 255

        # Wind speed.
        self.domeinf["WINDSPD"] = 255

        # Temperature.
        self.domeinf["TEMP"] = 255

        # Humidity.
        self.domeinf["HUMID"] = 255

        # Wetness.
        self.domeinf["WETNESS"] = 255

        # Snow.
        self.domeinf["SNOW"] = 255

        # Windspeed peak.
        self.domeinf["WINDPEAK"] = 255

        # Scope azimuth.
        self.domeinf["SCOPEAZ"] = 999

        # Internal "deadzone".
        self.domeinf["INTDZ"] = 3

        # Internal offset.
        self.domeinf["INTOFF"] = 0

        # Additional values not used in info packet.

        # Offset from the values read from barcode reader to get correct az.
        self.domeinf["DOMEOFF"] = 8

        # Azimuth value used to message the rotating dome to abort.
        self.domeinf["ABORT"] = 0

    def setInf(self, keyword, value):
        #    print("setInf: " + keyword + " " + str(value))
        self.domeinf[keyword] = value

    def getInf(self, keyword):
        #    print("getInf: " + keyword)
        return self.domeinf.get(keyword)

    def getInfPack(self):
        # Assemble a string of bytes representing the info packet and return.
        print("InfPacket: Returning Packet")
        istring = self.domeinf["Verstr"]
        for key in list(self.domeinf)[1:4]:
            istring += ","
            istring += str(self.domeinf[key])
        istring += ","
        istring += str((self.domeinf["ADAZ"] - self.domeinf["DOMEOFF"]) % 360)
        for key in list(self.domeinf)[5:]:
            istring += ","
            istring += str(self.domeinf[key])
        istring += "\n"
        infpacket = bytes(istring, "utf-8")
        return infpacket
