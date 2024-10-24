from typing import *



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
        