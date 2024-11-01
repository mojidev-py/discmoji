"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from ._http import HttpManager
import asyncio
from .intents import BotIntents
import websockets
from .types import WebsocketPayload
import contextlib
from contextlib import asynccontextmanager
from typing import Self

class DiscordWebsocket:
    def __init__(self,http: HttpManager,intents: BotIntents):
        self.ws = None
        self.token = http.token
        self.intents = intents
    
    @asynccontextmanager
    # huge credit to graingert on discord!
    async def initiate_connection(cls,ws: websockets.WebSocketClientProtocol,http: HttpManager,intents: BotIntents):
        async with websockets.connect(asyncio.run(http.request('get','/gateway/bot',True)).data["url"]) as ws:
                cls.ws = ws
                try:
                    goingtobeyield: Self = cls(ws,http,intents)
                    yield goingtobeyield
                except websockets.ConnectionClosedError:
                    raise RuntimeError("Gateway closed connection.")
                    
    
    async def _recieve_latest(self):
        return WebsocketPayload(await self.ws.recv())

    async def _hand_shake(self):
        ...