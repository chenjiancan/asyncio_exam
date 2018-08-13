# coding=utf-8
import asyncio
import aiohttp
import async_timeout

async def fetch_page_from(session, url):

    # with aiohttp.Timeout(10):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            if response.status != 200:
                print("response for {0} not ok".format(url))
            else:
                print("response for {0} ok".format(url))
                return await response.read()

async def main():
    url = "https://python.org"

    # should used async with within a coroutine
    async with aiohttp.ClientSession(loop=asyncio.get_event_loop()) as session:
        # with aiohttp.ClientSession(loop=loop) as session:
        result = await fetch_page_from(session, url)
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
