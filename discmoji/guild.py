from typing import *
from .member import GuildMember
import aiohttp
import asyncio
from _http import EndpointManager
class Guild:
    """Represents a discord server.
    This class will be provided. Do not try to initalize this class."""
    def __init__(self,_data: dict,__httpmanager: EndpointManager):
        self.user = ...
        # not yet, since i need to implement the user object
        self.http = __httpmanager
        self.id: int = int(_data["id"])
        self.name: int = _data["name"]
        self.icon: str = _data["icon"]
        self.splash: str = _data["splash"]
        self.owner_id: int = _data["owner_id"]
        self.afk_channel_id: int = _data["afk_channel_id"]
        self.afk_timeout: int = _data["afk_timeout"]
        self.verification_level: int = _data["verification_level"]
        self.message_notif_level: int = _data["default_message_notifications"]
        self.explicit_content_filter_level: int = _data["explicit_content_filter"]
        # for self.roles, once I make Role object, type hint will be more clarified
        self.roles: List = _data["roles"] 
        # same as self.roles notice
        self.emojis: List = _data["emojis"]
        self.features: List = _data["features"]
        self.mfa_level: int = _data["mfa_level"]
        self.app_id: int = _data["application_id"]
        self._member_cache: List[GuildMember] = []
        
        # rest will be included later
    
    
    
    
    
    async def get_member(self,username: str):
        """Gets the specified member from the guild, using their username."""
        # only using username because in prefix commands, GuildMember's user property is left blank
        
        for member in self._member_cache:
            if member.nick == username:
                return member
        return GuildMember(self.http.send_request('get',f'/guilds/{self.id}/members/search?query="{username}"'))
        