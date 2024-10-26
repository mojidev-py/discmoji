from typing import *
import aiohttp
import asyncio
from .types import Payload, OPCODES
import json
from .errors import DiscmojiRatelimit, DiscmojiAPIError
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

    async def send_request(
        self, method: Literal["get", "post", "put", "patch", "delete", "head", "options"], route: str, data: Optional[Dict] = None
    ) -> Payload:
        async with self.httpclient as client:
            try:
                match method:
                    case "get":
                        sent = await client.get(self.base_url + route)
                    case "post":
                        sent = await client.post(self.base_url + route, json=data)
                    case "put":
                        sent = await client.put(self.base_url + route, json=data)
                    case "patch":
                        sent = await client.patch(self.base_url + route, json=data)
                    case "delete":
                        sent = await client.delete(self.base_url + route)
                    case "head":
                        sent = await client.head(self.base_url + route)
                    case "options":
                        sent = await client.options(self.base_url + route)
                    case _:
                        raise ValueError(f"Unsupported HTTP method: {method}")

                parsed = await sent.read()
                decoded = await parsed.decode(encoding="utf-8")
                check = await self.ratelimited(sent)
                if check[0] == True:
                    warnings.warn(DiscmojiRatelimit(f"{check[1]}"))
                return Payload(code=OPCODES.HTTP, d=json.loads(decoded), event_name="HTTP_REQUEST_RECEIVED")
            except aiohttp.ClientError as e:
                raise DiscmojiAPIError(f"HTTP request failed: {e}")

    async def send_head_request(self, route: str) -> Payload:
        return await self.send_request("head", route)

    async def send_options_request(self, route: str) -> Payload:
        return await self.send_request("options", route)
