# coding=utf-8
import asyncio

async def on_client_connected(reader, writer):
    print("connected")
    loop = asyncio.get_event_loop()

    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Close the client socket")
    writer.close()

async def main():
    # create tcp server
    print("start server!")

    # start_server is a coroutine, await it
    server = await asyncio.start_server(client_connected_cb=on_client_connected, host="127.0.0.1", port=8090,
                         loop=asyncio.get_event_loop())
    print('Serving on {}'.format(server.sockets[0].getsockname()))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

    loop.close()