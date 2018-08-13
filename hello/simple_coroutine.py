# coding=utf-8
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print("say {0} on {1}".format(what, when))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # run one task in even loop until task done
    loop.run_until_complete(say("hello", 2))
    loop.close()
