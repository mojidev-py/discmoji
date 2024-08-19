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
SOFTWARE."""
import aiohttp
from typing import *
import asyncio
from .bot import cached_token
if TYPE_CHECKING:
    from .message import Message

class Original:
    """Represents the context the command is being invoked from."""
    def init(self):
        self.author = None # This equals None because this will be changed
        self.guild = None 
        self.base_url = "https://discord.com/api/v10"
        self.headers = {"Authorization":f"Bot {cached_token}"}
        self.msgclient = aiohttp.ClientSession(base_url=self.base_url,headers=self.headers)
        # only this for now, might find some more stuff later
        
    
    def _fill_attrs(self):
        # _fill_attrs() runs internally in the command decorator to fill in data about the user, guild, and more.
        ...
    
    async def send_message(self,content: str):
        """Sends a message in the channel the command was invoked from."""

        ...
        