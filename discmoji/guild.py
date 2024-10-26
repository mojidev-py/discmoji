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
    def __init__(self,_data: dict,__httpmanager: EndpointManager):
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
        # for self.roles, once I make Role object, type hint will be more clarified
        self.roles: Optional[List[Role]] = [Role(role) for role in _data.get("roles") if _data.get("roles") is not None] 
        # same as self.roles notice
        self.emojis: Optional[List[Emoji]] = [Emoji(emoji) for emoji in _data.get("emojis") if _data.get("emojis") is not None]
        self.features: Optional[List] = _data.get("features")
        self.mfa_level: Optional[int] = _data.get("mfa_level")
        self.app_id: Optional[int] = _data.get("application_id")
        self._member_cache: List[GuildMember] = []
        
        # rest will be included later
    
    
    
    
    
    async def get_member(self,username: Optional[str]):
        """Gets the specified member from the guild, using their username."""
        # only using username because in prefix commands, GuildMember's user property is left blank
        
        for member in self._member_cache:
            if member.nick == username:
                return member
        return GuildMember(asyncio.run(self.http.send_request('get',f'/guilds/{self.id}/members/search?query="{username}"')).data)
        
    async def update(self):
        """Updates the outdated objects."""
        updated_data = await self.http.send_request('get', f'/guilds/{self.id}')
        self.__init__(updated_data, self.http)
