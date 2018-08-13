# coding=utf-8
import asyncio


async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8090, loop=asyncio.get_event_loop())
    message = "hi"
    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
