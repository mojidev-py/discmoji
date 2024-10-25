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
from ._http import EndpointManager
from .gateway import GatewayManager
import asyncio
from .command import Command
from .guild import Guild
from .types import OPCODES
from .intents import BotIntents
from .context import Invoked

class CommandManager:
    def __init__(self, bot: 'Bot'):
        self.bot = bot
        self._all_cmds: List[Command] = []

    def command(self, name: str):
        """A decorator that registers a command with the specified name."""
        def decor(func: Callable):
            self._all_cmds.append(Command(name=name))
            return Command(name=name)
        return decor

class GuildManager:
    def __init__(self, bot: 'Bot'):
        self.bot = bot
        self._guild_cache: List[Guild] = []

    async def get_guild(self, id: int) -> Guild | None:
        """Gets a guild from the bot's current joined guilds, through the id."""
        for guild in self._guild_cache:
            if guild.id == id:
                return guild
        response = await self.bot._http.send_request('get', f"/guilds/{id}")
        return Guild(response.data)

    async def total_guilds(self) -> int:
        """Returns the total number of guilds the bot is in."""
        return self.bot._gateway_client.guild_count

    def _all_guilds_setter(self):
        # since the discord API lazily loads the guilds, this may not be an accurate count.
        if self.bot._gateway_client.current_payload.event_name == "GUILD_CREATE":
            self.bot.all_guilds: List[Guild] = []
            self.bot.all_guilds.append(Guild(self.bot._gateway_client.current_payload.data))

class Bot:
    """Represents the application."""
    def __init__(self, token: str, intents: BotIntents, prefix: str):
        self._http = EndpointManager(token=token)
        self._gateway_client = GatewayManager(token=token, intents=intents.result_field, endpointclient=self._http)
        self.token = token
        self.intents = intents.result_field
        self.command_manager = CommandManager(self)
        self.guild_manager = GuildManager(self)
        self.prefix = prefix
        self.info = self._gateway_client.captured_app_info

    async def connect(self):
        # this just inits the gateway connection
        await self._gateway_client._hand_shake()
        # self-explanatory, handles the heartbeats
        await self._gateway_client._handle_heartbeats()
        self.guild_manager._all_guilds_setter()
        if self._gateway_client.current_payload.code == OPCODES.RECONNECT:
            await self._gateway_client._reconnect_with_data()
        invokedsetup: Invoked = Invoked(self._http, self._gateway_client, self, self._gateway_client.current_payload.data["id"] if self._gateway_client.current_payload.data["id"] is not None else None)
        await invokedsetup.invoked_cmd_handler()

class ScalableBot(Bot):
    pass
