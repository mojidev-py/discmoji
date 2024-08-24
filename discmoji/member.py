from typing import *




class GuildMember:
    """Represents a discord member in a guild.."""
    def __init__(self,
    nick: str	,
    avatar: str	,
    roles: List[int]	,
    joined_at: int	,
    premium_since: int	,
    deaf: bool 	,
    mute: bool 	,
    flags: int	,
    pending: bool	,
    permissions: str	,
    muted_until: int,	
    avatar_decoration_data: None ): # for now
        self.nick = nick
        self.avatar = avatar
        self.roles = roles
        self.joined_at = joined_at
        self.premium_since = premium_since
        self.deaf = deaf
        self.mute = mute
        self.flags = flags
        self.pending = pending
        self.permissions = permissions
        self.muted_until = muted_until
        self.avatar_decoration_data = avatar_decoration_data