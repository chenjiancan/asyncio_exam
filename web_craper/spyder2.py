# coding=utf-8
import asyncio

import time
from contextlib import closing


async def get_page(host, port, wait=0):
    """Get a "web page" asynchronously.
    """
    # connect
    reader, writer = await asyncio.open_connection(host, port)

    # send request
    req = "\r\n".join((
        "GET /delay/{} HTTP/1.0".format(wait),
        "host: {}".format(host),
        "",""
    ))
    req_data = req.encode()
    writer.write(req_data)

    # recv response
    # reponse header
    response_header = []
    async for line_data in reader:
        line  = line_data.decode().strip()
        if not line:
            break
        response_header.append(line)

    # response body
    body = []
    async for line_data in reader:
        line  = line_data.decode().strip()
        if not line:
            break
        body.append(line)

    response = {
        "header": "\n".join(response_header),
        "body": "\n".join(body)
    }

    await writer.drain()
    writer.close()
    return response



"""Get "web pages.

Waiting until one pages is download before getting the next."
"""
def get_multiple_pages(host, port, waits, show_time=True):
    """Get multiple pages.
    """
    future = asyncio.gather(*(
        get_page(host, port, wait) for wait in waits
    ))
    loop = asyncio.get_event_loop()
    pages = loop.run_until_complete(future)
    return pages

def main():
    """Test it.
    """
    pages = get_multiple_pages(host='httpbin.org', port=80,
                               waits=[1, 5, 3, 2])
    for page in pages:
        print(page)


if __name__ == '__main__':

    main()