async def recv(r):
  while True:
    msg = await r.readexactly(4)
    if msg.rstrip() == b'DONE':
      print('Done receiving')
      break

    print(f'received: {msg.rstrip().decode()}')
    # respond to message.

async def send(w, msg):
  w.write(msg)
  print(f'sent: {msg.decode().rstrip()}')

async def DomeIO():
  # setup serial read
  # setup serial write
  received = recv(reader)
  await asyncio.wait([received])

if __name__ == '__main__':
  async.run(DomeIO())