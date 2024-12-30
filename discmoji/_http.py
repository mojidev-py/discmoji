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
from ._types import RequestBody
from typing import Callable,Any
from .exceptions import InternalDiscmojiException
class HttpManager:
   """Internal class that manages requests to endpoints."""
   def __init__(self,token: str):
        self.base_url = "https://discord.com"
        self.version = "/api/v10/"
        self.token = token
        self.normal = {"User-Agent":"DiscordBot (https://github.com/mojidev-py/discmoji,0.0.1)","Content-Type":"application/json"}
        self.auth = {"Authorization":f"Bot {self.token}"}
        
    

   async def request(self,method: str, route: str,auth: bool = False, data: dict = None, **kwargs):
        headers = self.normal | self.auth if auth else self.normal
        async with aiohttp.ClientSession(base_url=self.base_url,headers=headers) as client:
                    methods: dict[str,Callable[[Any],Any]] = {
                        "get": client.get,
                        "post": client.post,
                        "patch": client.patch,
                        "delete": client.delete,
                        "put": client.put
                    }
                    async with methods[method](url=f"{self.version}{route}",json=data if data else None,params=kwargs) as response:
                         return RequestBody(response)
                                               