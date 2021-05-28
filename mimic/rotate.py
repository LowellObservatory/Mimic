import asyncio

from .GPIOControl import GPIOControl


async def main(loop):
    gpio = GPIOControl()
    reck = test(gpio, 300)
    await asyncio.wait([reck])


async def test(gpio, wait):
    await gpio.rotate_right(wait)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
