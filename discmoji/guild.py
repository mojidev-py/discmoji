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
        self.id: int = self._get_dict_value(_data, "id")
        self.name: int = self._get_dict_value(_data, "name")
        self.icon: str = self._get_dict_value(_data, "icon")
        self.splash: str = self._get_dict_value(_data, "splash")
        self.owner_id: int = self._get_dict_value(_data, "owner_id")
        self.afk_channel_id: int = self._get_dict_value(_data, "afk_channel_id")
        self.afk_timeout: int = self._get_dict_value(_data, "afk_timeout")
        self.verification_level: int = self._get_dict_value(_data, "verification_level")
        self.message_notif_level: int = self._get_dict_value(_data, "default_message_notifications")
        self.explicit_content_filter_level: int = self._get_dict_value(_data, "explicit_content_filter")
        self.roles: List = self._get_dict_value(_data, "roles", [])
        self.emojis: List = self._get_dict_value(_data, "emojis", [])
        self.features: List = self._get_dict_value(_data, "features", [])
        self.mfa_level: int = self._get_dict_value(_data, "mfa_level")
        self.app_id: int = self._get_dict_value(_data, "application_id")
        self._member_cache: List[GuildMember] = []
        
        # rest will be included later

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
    
    async def get_member(self,username: str):
        """Gets the specified member from the guild, using their username."""
        # only using username because in prefix commands, GuildMember's user property is left blank
        
        for member in self._member_cache:
            if member.nick == username:
                return member
        return GuildMember(asyncio.run(self.http.send_request('get',f'/guilds/{self.id}/members/search?query="{username}"')).data)
        