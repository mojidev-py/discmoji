from typing import *
import aiohttp
from .overwrites import ChannelPermissionOverwrite
from ._http import EndpointManager
from .guild import Guild

class GuildTextChannel:
    def __init__(self, _data: dict, __bindedhttp: EndpointManager):
        self.id: Optional[int] = int(_data.get("id")) if _data.get("id") is not None else None
        self.name = _data.get("name")
        self.guild = None
        self.type = 0
        self.position: Optional[int] = _data.get("position")
        self.topic: Optional[str] = _data.get("topic")
        self.rate_limit: Optional[int] = _data.get("rate_limit_per_user")
        self.category_id: Optional[int] = _data.get("parent_id")
        self.last_pin: Optional[int] = _data.get("last_pin_timestamp")
        self.invoked_permissions: Optional[int] = _data.get("permissions")
        self.flags: Optional[int] = _data["flags"]
        self.messages_sent: Optional[int] = _data.get("total_message_sent")
        self.overwrites = [ChannelPermissionOverwrite(permissionoverwrite) for permissionoverwrite in _data.get("permission_overwrites")] if _data.get("permission_overwrites") is not None else None
        self.__bindedhttp = __bindedhttp

    async def initialize(self):
        if self.guild is None and self.id is not None:
            guild_data = await self.__bindedhttp.send_request('get', f'/guilds/{self.id}')
            self.guild = Guild(guild_data)
