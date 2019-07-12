import asyncio
from random import choice
from string import ascii_letters, digits

from aiohttp import web

WS_STRING_LENGTH = 100


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    response_alphabet = ascii_letters + digits
    while True:
        s = ''.join(choice(response_alphabet) for _ in range(WS_STRING_LENGTH))
        await ws.send_str(s)
        await asyncio.sleep(1)


async def client_handler(request):
    return web.FileResponse('./client.html')


def main():
    app = web.Application()
    app.add_routes([web.get('/', client_handler)])
    app.add_routes([web.get('/ws', websocket_handler)])
    web.run_app(app)


if __name__ == '__main__':
    main()
