# coding=utf-8
import asyncio

async def run_command(*args):

    process = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    print("communicate return")
    return stdout.decode()


if __name__ == '__main__':
    loop = asyncio.ProactorEventLoop()  # windows uses SelectorEventLoop as default, which not support subprocess
    asyncio.set_event_loop(loop)

    loop = asyncio.get_event_loop()

    result1, result2  = loop.run_until_complete(asyncio.gather(
        run_command("ls"),
        run_command("pwd")
    ))

    print("result \n\tls: \n{0} \n\tpwd: {1}".format(result1, result2))

