from typing import *
import aiohttp
from .overwrites import ChannelPermissionOverwrite
import asyncio
from ._http import EndpointManager
from .guild import Guild

class GuildTextChannel:
    def __init__(self, _data: dict, __bindedhttp: EndpointManager):
        self.id: Optional[int] = int(_data.get("id")) if _data.get("id") is not None else None
        self.type = 0
        self.position: Optional[int] = _data.get("position")
        self.overwrites = [ChannelPermissionOverwrite(permissionoverwrite) for permissionoverwrite in _data.get("permission_overwrites")] if _data.get("permission_overwrites") is not None else None
        self.guild = Guild(asyncio.run(__bindedhttp.send_request('get', f'/guilds/{_data.get("guild_id")}'))) if _data.get("guild_id") is not None else None
        self.name = _data.get("name")
        self.topic: Optional[str] = _data.get("topic")
        self.rate_limit: Optional[int] = _data.get("rate_limit_per_user")
        self.category_id: Optional[int] = _data.get("parent_id")
        self.last_pin: Optional[int] = _data.get("last_pin_timestamp")
        self.invoked_permissions: Optional[int] = _data.get("permissions")
        self.flags: Optional[int] = _data["flags"]
        self.messages_sent: Optional[int] = _data.get("total_message_sent")

    async def create_channel(self, guild_id: int, name: str, type: int = 0, topic: Optional[str] = None, rate_limit: Optional[int] = None, category_id: Optional[int] = None) -> 'GuildTextChannel':
        data = {
            "name": name,
            "type": type,
            "topic": topic,
            "rate_limit_per_user": rate_limit,
            "parent_id": category_id
        }
        response = await self.__bindedhttp.send_request('post', f'/guilds/{guild_id}/channels', data=data)
        return GuildTextChannel(response.data, self.__bindedhttp)

    async def delete_channel(self, channel_id: int):
        await self.__bindedhttp.send_request('delete', f'/channels/{channel_id}')

    async def edit_channel(self, channel_id: int, name: Optional[str] = None, topic: Optional[str] = None, rate_limit: Optional[int] = None, category_id: Optional[int] = None):
        data = {
            "name": name,
            "topic": topic,
            "rate_limit_per_user": rate_limit,
            "parent_id": category_id
        }
        await self.__bindedhttp.send_request('patch', f'/channels/{channel_id}', data=data)

    async def set_permissions(self, overwrite_id: int, allow: int, deny: int, type: int):
        data = {
            "id": overwrite_id,
            "allow": allow,
            "deny": deny,
            "type": type
        }
        await self.__bindedhttp.send_request('put', f'/channels/{self.id}/permissions/{overwrite_id}', data=data)

    async def delete_permission(self, overwrite_id: int):
        await self.__bindedhttp.send_request('delete', f'/channels/{self.id}/permissions/{overwrite_id}')
