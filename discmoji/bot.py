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
from .types import (GatewayManager,EndpointManager)
import functools
import asyncio
from .command import Command
from .guild import Guild
from .member import GuildMember


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
    async def connect(self):
        # this just inits the gateway connection
        await self._gateway_client._hand_shake()
        # self-explanatory, handles the heartbeats
        loop = asyncio.new_event_loop()
        # creates a loop that runs forever, and will stop if a Resume or Reconnect is called
        loop.create_task(self._gateway_client._handle_heartbeats)
        loop.run_forever()
    
    def command(self,name: str) -> Command:
        """A decorator that registers a command with the specified name."""
        
        def actual_deco(func: Coroutine):
            @functools.wraps(func)
            def decorator(*args, **kwargs):
                cmd = Command(name,(args,kwargs),func)
                self._all_cmds.append(cmd)
                return cmd
            return decorator
        return actual_deco
    
    async def get_guild(self,id: int) -> Guild:
        """Gets a guild from the bot's current joined guilds, through the id."""
        check = None
        for guild in self._guild_cache:
            if guild.id == id:
                check = True
                return guild
        if not check:
            guild = Guild(asyncio.run(self._http.send_request('get',f"/guilds/{id}")).data)
            self._guild_cache.append(guild)
            return guild
                
                
    
