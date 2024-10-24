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

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
    

    def _construct(self):
        # constructs itself so it can be used while running a command
        self.member: GuildMember = GuildMember(self._get_dict_value(self._gateway.current_payload.data, "member"))
        self.guild: Guild = Guild(asyncio.run(self._endpoint.send_request(method="get",route=f"/guilds/{self._get_dict_value(self._gateway.current_payload.data, 'guild_id')}")).data)
        self.channel: GuildTextChannel = GuildTextChannel(asyncio.run(self._endpoint.send_request('get',f'/channels/{self._get_dict_value(self._gateway.current_payload.data, "channel_id")}')).data)
        self.message: Message | None = Message(asyncio.run(self._endpoint.send_request('get',f'/channels/{self.channel.id}/messages/{self.__msgid}')).data)
    
    
    async def send_message(self,text: Optional[str],embeds: Embed | List[Embed] | None) -> Message:
        embed: Embed | None = None
        if embeds is not None:
            if len(embeds) == 1:
                embed = embeds._dictize()
                if text is None:
                    msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages',data={
                        "embeds": [embed]
                    })
                    read = await msg.read()
                    decode = read.decode()
                    returned = json.loads(decode)
                    return Message(Payload(None,returned,None,None).data)
                else:
                    msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages',data={
                        "content": text,
                        "embeds": [embed]
                    })
                    read = await msg.read()
                    decode = read.decode()
                    returned = json.loads(decode)
                    return Message(Payload(None,returned,None,None).data)
            if len(embeds) > 1:
                listembeds: list[Embed] = [_._dictize() for _ in embeds]
                if text is None:
                        msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages',data={
                        "embeds": listembeds
                    })
                        read = await msg.read()
                        decode = read.decode()
                        returned = json.loads(decode)
                        return Message(Payload(None,returned,None,None).data)
                else:
                            msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages',data={
                        "content": text,
                        "embeds": listembeds
                        })
                            read = await msg.read()
                            decode = read.decode()
                            returned = json.loads(decode)
                            return Message(Payload(None,returned,None,None).data)
                
                
                    
                        
        else:
            msg = await self._endpoint.httpclient.post(f'/channels/{self.channel.id}/messages',data={
            "content": text
        })
            read = await msg.read()
            recved = read.decode()
            tobepayloaded = json.loads(recved)
            return Message(Payload(None,tobepayloaded,None,None).data)
    


    
    
    async def invoked_cmd_handler(self):
        asyncio.sleep(5.5)
        # checks every 5.5 seconds for new commands
        n = 0
        if self._gateway.current_payload.event_name == "MESSAGE_CREATE":
            for cmd in self._bot._all_cmds:
                if cmd.name in self._gateway.current_payload.data["content"]:
                    self._construct()
                    args: str = self._gateway.current_payload.data["content"]
                    argsfilter = args.removeprefix(f"{self._bot.prefix}{cmd.name} ")
                    final1 = args.split(maxsplit=cmd.callback.__code__.co_argcount)
                    for arg in enumerate(final1):
                        if arg[1].isnumeric():
                            final1[arg[0]] = int(arg)
                            
                    await cmd.callback(self,*final1)
 
                    
                    
                        
                            
