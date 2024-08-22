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
if TYPE_CHECKING:
    from .message import Message
    from .bot import Bot

class Original:
    """Represents the context the command is being invoked from."""
    def init(self,bot: Bot):
        self.author = None # This equals None because this will be changed
        self.guild = None 
        self.base_url = "https://discord.com/api/v10"
        self.bot = bot
        self.reggedcmds = bot.cmds
        self.channel_id = bot.channelid
        self.headers = {"Authorization":f"Bot {self.bot._get_token()}"}
        self.msgclient = aiohttp.ClientSession(base_url=self.base_url,headers=self.headers)
        # only this for now, might find some more stuff later
        # channel id will be filled out with _fill_attrs()
    
    def _fill_attrs(self):
        ...
        # this will make the author attr. a member and the guild a guild
        
    async def send_message(self,content: str):
        """Sends a message in the channel the command was invoked from."""
        async with self.msgclient:
            self.msgclient.post(url=self.base_url.join(f"/channels/{self.channel_id}/messages"),json={
                "content": content,
                "tts": False, # tts will always default to false
            })
    

        