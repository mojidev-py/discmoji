from typing import *
from ._http import EndpointManager
from .gateway import GatewayManager
import asyncio
from .bot import Bot
from .member import GuildMember
from .guild import Guild
from .channel import GuildTextChannel
from .message import Message
from .messagesubtypes import *
from .types import Payload
import json

class Invoked:
    """A class that hosts the data of where a prefix/slash command was used."""
    # A class that hosts the data of where a command was used
    def __init__(self,endpoint: EndpointManager,gateway: GatewayManager,bot: Bot,msgid: int | None):
        self._endpoint = endpoint
        self._gateway = gateway
        self._bot = bot
        # rest will be constructed by internal funcs
        self.member = ...
        self.message = ...
        self.channel = ...
        self.guild = ...
        self.__msgid = msgid
    

    async def _construct(self):
        # constructs itself so it can be used while running a command
        self.member: GuildMember = GuildMember(self._gateway.current_payload.data["member"])
        guild_data = await self._endpoint.send_request(method="get", route=f"/guilds/{self._gateway.current_payload.data['guild_id']}")
        self.guild: Guild = Guild(guild_data.data)
        channel_data = await self._endpoint.send_request('get', f'/channels/{self._gateway.current_payload.data["channel_id"]}')
        self.channel: GuildTextChannel = GuildTextChannel(channel_data.data)
        message_data = await self._endpoint.send_request('get', f'/channels/{self.channel.id}/messages/{self.__msgid}')
        self.message: Message | None = Message(message_data.data)
    
    
    async def send_message(self, text: Optional[str] = None, embeds: Optional[Union[Embed, List[Embed]]] = None) -> Message:
        data = {}
        if text:
            data["content"] = text
        if embeds:
            if isinstance(embeds, Embed):
                data["embeds"] = [embeds._dictize()]
            else:
                data["embeds"] = [embed._dictize() for embed in embeds]
        msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages', json=data)
        read = await msg.read()
        decode = read.decode()
        returned = json.loads(decode)
        return Message(Payload(None, returned, None, None).data)
    
    async def invoked_cmd_handler(self):
        await asyncio.sleep(5.5)
        # checks every 5.5 seconds for new commands
        n = 0
        if self._gateway.current_payload.event_name == "MESSAGE_CREATE":
            for cmd in self._bot._all_cmds:
                if cmd.name in self._gateway.current_payload.data["content"]:
                    await self._construct()
                    args: str = self._gateway.current_payload.data["content"]
                    argsfilter = args.removeprefix(f"{self._bot.prefix}{cmd.name} ")
                    final1 = args.split(maxsplit=cmd.callback.__code__.co_argcount)
                    for arg in enumerate(final1):
                        if arg[1].isnumeric():
                            final1[arg[0]] = int(arg)
                            
                    await cmd.callback(self,*final1)
