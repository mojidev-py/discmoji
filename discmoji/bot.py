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
from .intents import BotIntents, IntentsBits
from ._http import HttpManager
from ._gateway import DiscordWebsocket
from .command import BotCommand
from ._types import logger
import asyncio
class Bot:
    """Represents your application."""
    def __init__(self,token: str,intents: BotIntents | IntentsBits,prefix: str):
        self.http = HttpManager(token)
        self.dws = DiscordWebsocket(self.http,intents)
        self.intents = intents
        self.prefix = prefix
        self.prefix_command = BotCommand
        """A decorator that registers a prefix command for this bot."""
        self.prefix_command.bot = self
        self._commands: list[BotCommand] = []
    
    
    async def _listen_for_cmd_invoke(self):
        async for message in self.dws.ws:
            # listens for message in gateway manager's (open) websocket, since it's going to be running in the async with below
            pass
    
    
    
    async def _connect(self):
        logger.info("Initiating connection process with gateway...")
        async with self.dws.initiate_connection(http = self.http,intents= self.intents) as connection:
            await connection._establish()
    
    def connect_thread(self):
        """An abstraction over `_connect()` that runs synchronously, for QoL purposes. \n
        this function is the only function you should use to connect your bot."""
        with asyncio.Runner() as runner:
            runner.run(self._connect())
    