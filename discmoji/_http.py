from typing import *
import aiohttp
import asyncio
from .types import Payload, OPCODES
import json
from .errors import DiscmojiRatelimit
import warnings


class EndpointManager:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://discord.com/api/v10"
        self.headers = {
            "User-Agent": "DiscordBot https://github.com/mojidev-py/discmoji, 0.0.1pr",
            "Authorization": f"Bot {token}",
        }
        self.httpclient = aiohttp.ClientSession(base_url=self.base_url, headers=self.headers)

    async def ratelimited(self, request: aiohttp.ClientResponse):
        if request.headers.get(key="Retry-After") is int and request.headers.get(key="Retry-After") > 0:
            return (True, request.headers.get(key="Retry-After"))
        return False

    async def _send(self, method: str, route: str) -> Payload:
        async with self.httpclient as client:
            sent = await client.request(method, self.base_url + route)
            parsed = await sent.read()
            decoded = await parsed.decode(encoding="utf-8")
            check = await self.ratelimited(sent)
            if check[0] == True:
                warnings.warn(DiscmojiRatelimit(f"{check[1]}"))
            return Payload(code=OPCODES.HTTP, d=json.loads(decoded), event_name="HTTP_REQUEST_RECEIVED")

    async def send_request(self, method: Literal['get', 'post', 'put', 'patch', 'delete'], route: str) -> Payload:
        return await self._send(method, route)
