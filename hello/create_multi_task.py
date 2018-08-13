# coding=utf-8
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print("say {0} on {1}".format(what, when))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # create tasks
    loop.create_task(say("hello", 2))
    loop.create_task(say("hi", 3))
    loop.create_task(say("hey", 1))

    # run task created in even loop
    loop.run_forever()

    print("all task done")  # would not happen here
    loop.close()
