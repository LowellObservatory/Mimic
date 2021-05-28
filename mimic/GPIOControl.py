import time
import asyncio

import RPi.GPIO as GPIO


class GPIOControl:
    def __init__(self):
        print("setting up the gpio board")
        GPIO.setmode(GPIO.BCM)
        self.chan_list = [5, 6, 16, 17, 22, 23, 24, 25, 26, 27]
        GPIO.setup(self.chan_list, GPIO.OUT)
        GPIO.output(self.chan_list, GPIO.HIGH)

    def abort(self, info):
        print("abort in GPIO")
        GPIO.output(self.chan_list, GPIO.HIGH)

    #    print("666")
    #    info.setInf("ABORT", 666)

    def upper_shutter_open(self, wait):
        print("GPIOControl: upper_shutter_open")
        GPIO.output([26, 23, 24], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        time.sleep(wait)
        GPIO.output([26, 23, 24], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    def upper_shutter_close(self, wait):
        print("GPIOControl: upper_shutter_close")
        GPIO.output([26, 23, 24], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        time.sleep(wait)
        GPIO.output([26, 23, 24], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    def lower_shutter_open(self, wait):
        print("GPIOControl: lower_shutter_open")
        GPIO.output([6, 25, 16], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        time.sleep(wait)
        GPIO.output([6, 25, 16], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    def lower_shutter_close(self, wait):
        print("GPIOControl: lower_shutter_close")
        GPIO.output([6, 25, 16], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        time.sleep(wait)
        GPIO.output([6, 25, 16], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    async def rotate_left(self, wait):
        print("GPIOControl: rotate_left")
        GPIO.output([27, 5, 17], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        await asyncio.sleep(wait)
        GPIO.output([27, 5, 17], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    async def rotate_right(self, wait):
        print("GPIOControl: rotate_right")
        GPIO.output([27, 5, 22], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        await asyncio.sleep(wait)
        GPIO.output([27, 5, 22], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    async def rotate_left_az(self, azimuth, info):
        print("GPIOControl: rotate_left_az")

        # 2 for coast
        targ_az = (int(azimuth) + info.getInf("DOMEOFF") + 2) % 360
        got_there = False

        # start rotation
        GPIO.output([27, 5, 17], (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        curr_az = int(info.getInf("ADAZ"))
        while not got_there:
            await asyncio.sleep(0.2)
            curr_az = int(info.getInf("ADAZ"))
            if curr_az <= (targ_az + 1) and curr_az >= (targ_az - 1):
                got_there = True
            if curr_az <= (targ_az + 1) and curr_az >= (targ_az - 10):
                got_there = True

        # end rotation
        GPIO.output([27, 5, 17], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    async def rotate_right_az(self, azimuth, info):
        print("GPIOControl: rotate_right_az")

        # 2 for coast
        targ_az = (int(azimuth) + info.getInf("DOMEOFF") - 2) % 360
        got_there = False

        # rotate
        GPIO.output([27, 5, 22], (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        curr_az = int(info.getInf("ADAZ"))
        while not got_there:
            await asyncio.sleep(0.2)
            curr_az = int(info.getInf("ADAZ"))
            if curr_az <= (targ_az + 1) and curr_az >= (targ_az - 1):
                got_there = True
            if curr_az <= (targ_az + 10) and curr_az >= (targ_az - 1):
                got_there = True

        # end rotation
        GPIO.output([27, 5, 22], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
