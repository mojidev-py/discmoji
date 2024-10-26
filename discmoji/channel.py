from typing import *
import aiohttp
from .overwrites import ChannelPermissionOverwrite
import asyncio
from ._http import EndpointManager
from .guild import Guild
class GuildTextChannel:
    def __init__(self,_data: dict,__bindedhttp: EndpointManager):
        self.id: Optional[int] = int(_data.get("id")) if _data.get("id") is not None else None
        self.type = 0       
        self.position: Optional[int] = _data.get("position")
        # will be an object once Intents are made
        # goes through each entry in the _data's perm overwrites and makes a class for each overwrite
        self.overwrites = [ChannelPermissionOverwrite(permissionoverwrite) for permissionoverwrite in _data.get("permission_overwrites")] if _data.get("permission_overwrites") is not None else None
        self.guild = Guild(asyncio.run(__bindedhttp.send_request('get',f'/guilds/{_data.get("guild_id")}'))) if _data.get("guild_id") is not None else None
        self.name = _data.get("name")
        self.topic: Optional[str] = _data.get("topic")
        self.rate_limit: Optional[int] = _data.get("rate_limit_per_user")
        self.category_id: Optional[int] = _data.get("parent_id")
        self.last_pin: Optional[int] = _data.get("last_pin_timestamp")
        self.invoked_permissions: Optional[int] = _data.get("permissions")
        self.flags: Optional[int] = _data["flags"]
        self.messages_sent: Optional[int] = _data.get("total_message_sent")
        
    async def update(self):
        """Updates the outdated objects."""
        updated_data = await self.__bindedhttp.send_request('get', f'/channels/{self.id}')
        self.__init__(updated_data, self.__bindedhttp)
