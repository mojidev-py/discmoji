from typing import *
from .member import GuildMember
import aiohttp
import asyncio
from _http import EndpointManager
from .user import User
from .roles import Role
from .emoji import Emoji

class Guild:
    """Represents a discord server.
    This class will be provided. Do not try to initalize this class."""
    def __init__(self, _data: dict, __httpmanager: EndpointManager):
        self.user: Optional[User] = User(_data.get("user")) if _data.get("user") is not None else None
        self.http: EndpointManager = __httpmanager
        self.id: Optional[int] = int(_data.get("id"))
        self.name: Optional[int] = _data.get("name")
        self.icon: Optional[str] = _data.get("icon")
        self.splash: Optional[str] = _data.get("splash")
        self.owner_id: Optional[int] = int(_data.get("owner_id"))
        self.afk_channel_id: Optional[int] = int(_data.get("afk_channel_id"))
        self.afk_timeout: Optional[int] = _data.get("afk_timeout")
        self.verification_level: Optional[int] = _data.get("verification_level")
        self.message_notif_level: Optional[int] = _data.get("default_message_notifications")
        self.explicit_content_filter_level: Optional[int] = _data.get("explicit_content_filter")
        self.roles: Optional[List[Role]] = [Role(role) for role in _data.get("roles") if _data.get("roles") is not None] 
        self.emojis: Optional[List[Emoji]] = [Emoji(emoji) for emoji in _data.get("emojis") if _data.get("emojis") is not None]
        self.features: Optional[List] = _data.get("features")
        self.mfa_level: Optional[int] = _data.get("mfa_level")
        self.app_id: Optional[int] = _data.get("application_id")
        self._member_cache: List[GuildMember] = []

    async def get_member(self, username: Optional[str]):
        """Gets the specified member from the guild, using their username."""
        for member in self._member_cache:
            if member.nick == username:
                return member
        return GuildMember(asyncio.run(self.http.send_request('get', f'/guilds/{self.id}/members/search?query="{username}"')).data)
    
    async def create_guild(self, name: str, region: Optional[str] = None, icon: Optional[str] = None, verification_level: Optional[int] = None, default_message_notifications: Optional[int] = None, explicit_content_filter: Optional[int] = None) -> 'Guild':
        data = {
            "name": name,
            "region": region,
            "icon": icon,
            "verification_level": verification_level,
            "default_message_notifications": default_message_notifications,
            "explicit_content_filter": explicit_content_filter
        }
        response = await self.http.send_request('post', '/guilds', data=data)
        return Guild(response.data, self.http)

    async def delete_guild(self, guild_id: int):
        await self.http.send_request('delete', f'/guilds/{guild_id}')

    async def edit_guild(self, guild_id: int, name: Optional[str] = None, region: Optional[str] = None, icon: Optional[str] = None, verification_level: Optional[int] = None, default_message_notifications: Optional[int] = None, explicit_content_filter: Optional[int] = None):
        data = {
            "name": name,
            "region": region,
            "icon": icon,
            "verification_level": verification_level,
            "default_message_notifications": default_message_notifications,
            "explicit_content_filter": explicit_content_filter
        }
        await self.http.send_request('patch', f'/guilds/{guild_id}', data=data)
    
    async def add_member(self, guild_id: int, user_id: int, access_token: str, nick: Optional[str] = None, roles: Optional[List[int]] = None, mute: Optional[bool] = None, deaf: Optional[bool] = None):
        data = {
            "access_token": access_token,
            "nick": nick,
            "roles": roles,
            "mute": mute,
            "deaf": deaf
        }
        await self.http.send_request('put', f'/guilds/{guild_id}/members/{user_id}', data=data)

    async def remove_member(self, guild_id: int, user_id: int):
        await self.http.send_request('delete', f'/guilds/{guild_id}/members/{user_id}')
