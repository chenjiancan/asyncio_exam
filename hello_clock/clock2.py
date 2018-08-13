# coding=utf-8
import asyncio


async def print_every_second():
    for i in range(60):
        print("{}s".format(i))
        await asyncio.sleep(1)


async def print_every_minute():
    while True:
        for i in range(1, 10):
            await print_every_second()
            print("{}m".format(i))

            # await asyncio.sleep(60)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        # gather add a list of task in to One future
        asyncio.gather(
            # print_every_second(),
            print_every_minute()
        )
    )
    loop.close()
