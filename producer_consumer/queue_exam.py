# coding=utf-8
import asyncio
import logging
import random

import os

# PYTHONASYNCIODEBUG=1
os.environ["PYTHONASYNCIODEBUG"] = "1"      # set environment variable
logging.basicConfig(level=logging.DEBUG)    # enable asyncio debug logging

async def produce(queue, n):
    for x in range(n):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)


async def consume(queue):
    count  = 0
    while True:
        # wait for an item from the producer
        item = await queue.get()

        # process the item
        print('consuming {}...'.format(item))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())

        # Notify the queue that the item has been processed
        # cause a counter inside queue count down to 0, that make queue.join() return
        queue.task_done()

        # 可以做个试验，把以下代码段往前移到 task_done 之前，会 queue.join() 会在 long wait 之后才返回，这说明 task_done 的作用
        count += 1
        if count == 10:
            await asyncio.sleep(5)
            print("long wait")



async def run(n):
    queue = asyncio.Queue()
    # schedule the consumer
    consumer = asyncio.ensure_future(consume(queue))   # add consume coroutine to loop as a future obj
    await asyncio.sleep(5)   # while waiting here, consume starts
    # run the producer and wait for completion
    await produce(queue, n)
    # wait until the consumer has processed all items
    await queue.join()
    print("queue joined")

    await asyncio.sleep(5)
    # the consumer is still awaiting for an item, cancel it
    consumer.cancel()
    print("consumer canceled")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(10))
    loop.close()