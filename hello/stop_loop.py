# coding=utf-8
import asyncio

import time


async def say(what, when):
    # time.sleep(1)
    # print("wake from time.sleep  (blocked) ")

    await asyncio.sleep(when)
    print("say {0} on {1}".format(what, when))


async def stop_after(when):
    print("task 'stop_after' start")
    await asyncio.sleep(when)
    print("stop on {}".format(when))
    asyncio.get_event_loop().stop()
    print("stopped")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # create tasks
    loop.create_task(stop_after(1))
    loop.create_task(say("hello", 2))
    loop.create_task(say("hi", 3))
    loop.create_task(say("hey", 1))

    # run task created in even loop
    loop.run_forever()

    print("all task done")  # would not happen here
    loop.close()

    # task 'stop_after' start
    # stop on 1
    # stopped
    # say hey on 1
    # all task done
    # Task was destroyed but it is pending!
    # task: <Task pending coro=<say() done, defined at D:/workspace/PycharmProjects/learn/asyncio_exam/hello/stop_loop.py:4> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x00000122987ED3A8>()]>>
    # Task was destroyed but it is pending!
    # task: <Task pending coro=<say() done, defined at D:/workspace/PycharmProjects/learn/asyncio_exam/hello/stop_loop.py:4> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x00000122988A55B8>()]>>

