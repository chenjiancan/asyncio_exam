# coding=utf-8

import asyncio

import time
import threading

def compute_exp(num):
    # implementation
    print("current_thread：　" +threading.current_thread().getName())
    # current_thread：　<concurrent.futures.thread.ThreadPoolExecutor object at 0x0000023611F7EC50>_0

    time.sleep(1)
    return num **2


async def main(loop):
    print("current_thread：　" +threading.current_thread().getName())

    result = await loop.run_in_executor(None, compute_exp, 20000)  # run in default thread pool
    print("result: %s" % result)

if __name__ == '__main__':
    print("current_thread：　" +threading.current_thread().getName())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()