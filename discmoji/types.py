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

import aiohttp
import asyncio
import json
from typing import Optional

class ResponseData:
    """Internal class that hosts data from HTTP requests."""
    def __init__(self,data: aiohttp.ClientResponse):
        self.code = data.status
        self.data: dict = json.loads(asyncio.run(data.content.read()).decode())
        self.headers = data.headers


class WebsocketPayload:
    """Internal class that hosts data from the Discord Gateway."""
    def __init__(self,payload: Optional[aiohttp.WSMessage], opcode: int | None,data: dict | str, seq: int):
        self.__serlized: dict = payload.json()
        self.opcode = self.__serlized["op"] if opcode is None else opcode
        self.data = self.__serlized["d"] if data is None else data
        self.seq = self.__serlized.get("s") if seq is None else seq
        self.event_name = self.__serlized.get("t")
        