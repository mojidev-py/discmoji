from typing import *
import aiohttp
from .overwrites import ChannelPermissionOverwrite
import asyncio
from ._http import EndpointManager
from .guild import Guild
class GuildTextChannel:
    def __init__(self,_data: dict,__bindedhttp: EndpointManager):
        self.id = int(_data["id"])
        self.type = 0       
        self.position = _data["position"]
        # will be an object once Intents are made
        # goes through each entry in the _data's perm overwrites and makes a class for each overwrite
        self.overwrites = [ChannelPermissionOverwrite(permissionoverwrite) for permissionoverwrite in _data["permission_overwrites"]]
        self.guild = Guild(asyncio.run(__bindedhttp.send_request('get',f'/guilds/{_data["guild_id"]}'))) if _data["guild_id"] is not None else None
        self.name = _data["name"]
        self.topic: str | None = _data["topic"]
        self.rate_limit: int = _data["rate_limit_per_user"]
        self.category_id: int = _data["parent_id"]
        self.last_pin: int = _data["last_pin_timestamp"]
        self.invoked_permissions: int | None = _data["permissions"]
        self.flags: int = _data["flags"]
        self.messages_sent: int = _data["total_message_sent"]
        
        