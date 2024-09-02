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

from typing import *
from .http import EndpointManager
from .gateway import GatewayManager
import functools
import asyncio
from .command import Command
from .guild import Guild
from .member import GuildMember
from .types import OPCODES


class Bot:
    """Represents the application."""
    def __init__(self,token: str,intents: int):
        self._http = EndpointManager(token=token)
        self._gateway_client = GatewayManager(token=token,intents=intents,endpointclient=self._http)
        self.token = token
        self.intents = intents
        self._all_cmds: List[Command] = []
        self._intern_context = None
        self._guild_cache: List[Guild] = []
        self.command = Command
        self.command.bot = self
    async def connect(self):
        # this just inits the gateway connection
        await self._gateway_client._hand_shake()
        # self-explanatory, handles the heartbeats
        loop = asyncio.new_event_loop()
        # creates a loop that runs forever, and will stop if Reconnect is called
        loop.create_task(self._gateway_client._handle_heartbeats)
        loop.run_forever()
        if self._gateway_client.current_payload.code == OPCODES.RECONNECT:
            loop.stop()
            # I need to add handling for reconnect
            ...
        
    
    
    async def get_guild(self,id: int) -> Guild:
        """Gets a guild from the bot's current joined guilds, through the id."""
        check = None
        for guild in self._guild_cache:
            if guild in self._guild_cache:
                check = True
                return guild
        if check is None:
            guild = Guild(asyncio.run(self._http.send_request('get',f"/guilds/{id}")))
            return guild
    
    async def total_guilds(self) -> int:
        """Returns the total number of guilds the bot is in."""
        return self._gateway_client.guild_count             
