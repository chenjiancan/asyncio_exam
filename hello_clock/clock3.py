# coding=utf-8
import asyncio

second = 0
minute = 0
hour = 0


async def task_second():
    global second
    while True:
        print("time is {0}:{1}:{2}".format(hour, minute, second))
        await asyncio.sleep(1)
        second = second + 1 if second + 1 < 60 else 0


async def task_minute():
    global minute
    while True:
        await asyncio.sleep(60)
        minute = minute + 1 if minute + 1 < 60 else 0


async def task_hour():
    global hour
    while True:
        await asyncio.sleep(60 * 60)
        hour = hour + 1 if hour + 1 < 24 else 0


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        # gather add a list of task in to One future
        asyncio.gather(
            task_second(),
            task_minute(),
            task_hour()
        )
    )
    loop.close()
