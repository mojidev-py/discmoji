from typing import *



class GuildMember:
    """Represents a member from a guild.
    Do not initalize this class, it will be initalized for you."""
    def __init__(self,_data: dict):
        # data is a dict because I didn't want all that clutter from having each field of member
        # in docs
        # all fields are optional because MESSAGE_CREATE provides a partial member obj
        self.nick: Optional[str] = self._get_dict_value(_data, "nick")
        self.avatar: Optional[str] = self._get_dict_value(_data, "avatar")
        self.roles: Optional[List[int]] = self._get_dict_value(_data, "roles", [])
        self.joined_at: Optional[int] = self._get_dict_value(_data, "joined_at")
        self.premium_since: Optional[int] = self._get_dict_value(_data, "premium_since")
        self.deafened: Optional[bool] = self._get_dict_value(_data, "deaf", False)
        self.muted: Optional[bool] = self._get_dict_value(_data, "mute", False)
        self.flags: Optional[int] = self._get_dict_value(_data, "flags")
        self.muted_until: Optional[int] = self._get_dict_value(_data, "communication_disabled_until")
        self.decoration_data: Optional[Dict[str,Any]] = self._get_dict_value(_data, "avatar_decoration_data")

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
