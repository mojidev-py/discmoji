from typing import *
from ._http import EndpointManager
from .gateway import GatewayManager
import asyncio
from .bot import Bot
from .member import GuildMember
from .guild import Guild
from .channel import GuildTextChannel
from .message import Message


class Invoked:
    """A class that hosts the data of where a prefix/slash command was used."""
    # A class that hosts the data of where a command was used
    def __init__(self,endpoint: EndpointManager,gateway: GatewayManager,bot: Bot,message: Message | None):
        self._endpoint = endpoint
        self._gateway = gateway
        self._bot = bot
        # rest will be constructed by internal funcs
        self.member = ...
        self.message: Message = Message(asyncio.run(self._bot._http.send_request('get',f'/channels/{self.channel.id}/messages/{self.message.id}')))
        self.channel = ...
        self.guild = ...
    

    def _construct(self):
        # constructs itself so it can be used while running a command
        self.member: GuildMember = GuildMember(self._gateway.current_payload.data["member"])
        self.guild: Guild = Guild(asyncio.run(self._endpoint.send_request(method="get",route=f"/guilds/{self._gateway.current_payload.data["guild_id"]}")).data)
        self.channel: GuildTextChannel = GuildTextChannel(asyncio.run(self._endpoint.send_request('get',f'/channels/{self._gateway.current_payload.data["channel_id"]}')).data)