"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import Optional
from ..user import User
from .guild import Guild
from ..snowflake import Snowflake
import datetime
from ..decoration import AvatarDecoration
class GuildMember:
    """Represents a member in a guild.
    ## Attributes
    - user - `discmoji.User | None`
        - contains the user object of the guild member. Will not be present in prefix command context.
    - nick - `Optional[str]`
        - contains the nickname of the guild member.
    - avatar - `Optional[str]`
        - contains the formatted CDN link of the guild member's avatar.
    - banner - `Optional[str]`
        - contains the formatted CDN link of the guild member's banner.
    - roles - `Optional[str]`
        - contains the role id's of the guild member. Role objects can be retrieved through `discmoji.Guild.get_role()`.
    - joined_at - `datetime.datetime`
        - contains the join date of the guild member, converted from ISO8601 format.
    - premium_since - `Optional[datetime.datetime]`
        - contains the time elapsed since the guild member first boosted the guild, converted from ISO8601 format.
    - deafened - `bool`
        - Indicates whether the guild member is deafened in a voice channel or not.
    - muted - `bool`
        - Indicates whether the guild member is muted in a voice channel or not.
    - pending - `Optional[bool]`
        - Indicates whether the guild member has passed membership screening or not.
    - timeout_until - `Optional[datetime.datetime]`
        - Contains the date that the guild member's timeout ends, if applicable, else is None.
    - avatar_decoration - `Optional[discmoji.AvatarDecoration]`
        - Contains the Avatar Decoration object, if it exists."""
    def __init__(self,_dict: dict[str,str | int | dict | None],__binded_guild: Guild):
        self.user: User | None = User(_dict.get("user")) if _dict.get("user") is not None else None 
        self.nick: Optional[str] = _dict.get("nick")
        self.avatar: Optional[str] = f"https://cdn.discordapp.com/guilds/{__binded_guild.id}/users/{self.user.id if self.user is User else None}/avatars/{_dict.get("avatar")}.{"gif" if _dict.get("avatar").startswith("a_") else "png"}"
        self.banner: Optional[str] = f"https://cdn.discordapp.com/guilds/{__binded_guild.id}/users/{self.user.id if self.user is User else None}/banners/{_dict.get("avatar")}.{"gif" if _dict.get("avatar").startswith("a_") else "png"}"
        self.roles: list[Snowflake] = [Snowflake(roleid) for roleid in _dict["roles"]]
        self.joined_at: datetime.datetime = datetime.datetime.fromisoformat(_dict["joined_at"])
        self.premium_since: Optional[datetime.datetime] = datetime.datetime.fromisoformat(_dict.get("premium_since"))
        self.deafened: bool = _dict.get("deaf")
        self.muted: bool = _dict.get("mute")
        self.pending: Optional[bool] = _dict.get("pending")
        self.timeout_until: Optional[datetime.datetime] = datetime.datetime.fromisoformat(_dict.get("communication_disabled_until")) if datetime.datetime.fromisoformat(_dict.get("communication_disabled_until")) > datetime.datetime.now() or _dict.get("communication_disabled_until") is not None else None
        self.avatar_decoration: Optional[AvatarDecoration] = AvatarDecoration(_dict.get("avatar_decoration_data")) if _dict.get("avatar_decoration_data") is not None else None
        