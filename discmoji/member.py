from typing import *



class GuildMember:
    """Represents a member from a guild.
    Do not initalize this class, it will be initalized for you."""
    def __init__(self,_data: dict):
        # data is a dict because I didn't want all that clutter from having each field of member
        # in docs
        # all fields are optional because MESSAGE_CREATE provides a partial member obj
        self.nick: Optional[str] = _data["nick"]
        self.avatar: Optional[str] = _data["avatar"]
        self.roles: Optional[List[int]] = _data["roles"]
        self.joined_at: Optional[int] = _data["joined_at"]
        self.premium_since: Optional[int] = _data["premium_since"]
        self.deafened: Optional[bool] = _data["deaf"]
        self.muted: Optional[bool] = _data["mute"]
        self.flags: Optional[int] = _data["flags"]
        self.muted_until: Optional[int] = _data["communication_disabled_until"]
        self.decoration_data: Optional[Dict[str,Any]] = _data["avatar_decoration_data"]
        
            