from typing import *
from ._http import EndpointManager

class GuildMember:
    """Represents a member from a guild.
    Do not initalize this class, it will be initalized for you."""
    def __init__(self,_data: dict):
        self.nick: Optional[str] = _data.get("nick")
        self.avatar: Optional[str] = _data.get("avatar")
        self.roles: Optional[List[int]] = _data.get("roles")
        self.joined_at: Optional[int] = _data.get("joined_at")
        self.premium_since: Optional[int] = _data.get("premium_since")
        self.deafened: Optional[bool] = _data.get("deaf")
        self.muted: Optional[bool] = _data.get("mute")
        self.flags: Optional[int] = _data.get("flags")
        self.muted_until: Optional[int] = _data.get("communication_disabled_until")
        self.decoration_data: Optional[Dict[str,Any]] = _data.get("avatar_decoration_data")

    async def edit_member(self, guild_id: int, user_id: int, nick: Optional[str] = None, roles: Optional[List[int]] = None, mute: Optional[bool] = None, deaf: Optional[bool] = None, channel_id: Optional[int] = None):
        data = {
            "nick": nick,
            "roles": roles,
            "mute": mute,
            "deaf": deaf,
            "channel_id": channel_id
        }
        await self._http.send_request('patch', f'/guilds/{guild_id}/members/{user_id}', data=data)

    async def add_role(self, guild_id: int, user_id: int, role_id: int):
        await self._http.send_request('put', f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    async def remove_role(self, guild_id: int, user_id: int, role_id: int):
        await self._http.send_request('delete', f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}')

    async def kick_member(self, guild_id: int, user_id: int):
        await self._http.send_request('delete', f'/guilds/{guild_id}/members/{user_id}')

    async def ban_member(self, guild_id: int, user_id: int, delete_message_days: Optional[int] = None, reason: Optional[str] = None):
        data = {
            "delete_message_days": delete_message_days,
            "reason": reason
        }
        await self._http.send_request('put', f'/guilds/{guild_id}/bans/{user_id}', data=data)

    async def unban_member(self, guild_id: int, user_id: int):
        await self._http.send_request('delete', f'/guilds/{guild_id}/bans/{user_id}')
