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
from ..snowflake import Snowflake
from typing import Optional
from ..types import VerificationLevels,_find_verification_level,DefaultMessageNotifLevel,_find_notif_level,ExplicitContentFilter,_find_expl_level,SystemChannelFlags,_get_system_flags
from .roles import Role
from .emoji import Emoji
class Guild:
    """Represents a Guild/Server on Discord.
    ## Attributes
    - id - `discmoji.Snowflake`
       - Contains the id of the guild.
    - name - `str`
       - Contains the name of the guild.
    - icon - `str`
       - Contains the formatted CDN link of the guild's icon.
    - splash - `str`
       - Contains the formatted CDN link of the guild's splash.
    - discovery_splash - `Optional[str]`
       - Contains the formatted CDN link of the guild's discovery splash, if it is eligible and the option is enabled.
    - owner - `Optional[bool]`
       - Only a non-None value if this guild was constructed through the `Get User Guilds` endpoint.
    - permissions - `Optional[str]`
       - Only a non-None value if this guild was constructed through the `Get User Guilds` endpoint.
    - afk_channel_id - `Optional[discmoji.Snowflake]`
       - Contains the channel id in which guild members are moved to when the pass the inactivity threshold.
    - afk_timeout - `int`
       - Contains the length of the timeout if the guild member has passed the inactivity threshold.
    - widget_enabled - `Optional[bool]`
       - Indicates whether a widget (invite) has been enabled on this guild. May be None.
    - widget_channel_id - `Optional[discmoji.Snowflake]`
       - Contains the channel id in which the guild's widget directs to. May be None.
    - verification_level - `dict[str,int]`
       - Contains a dict with one key, which can be one of 5 string literals: `NONE`,`LOW`,`MEDIUM`,`HIGH`,`VERY_HIGH`, and whose value corresponds an int in the range of 0 to 4.
    - default_msg_notifs - `dict[str,int]`
       - Contains a dict with one key, which can be one of 2 string literals: `ALL_MESSAGES`,`ONLY_MENTIONS`, and whose value corresponds to an int in the range of 0 to 1.
    - explicit_filter_lvl - `dict[str,int]`
       - Contains a dict with one key, which can be one of 3 string literals: `DISABLED`,`MEMBERS_WITHOUT_ROLES`,`ALL_MEMBERS` and whose value corresponds an int in the range of 0 to 2.
    - roles - `list[discmoji.Role]`
       - Contains a list of all the guild's roles.
    - emojis - `list[discmoji.Emoji]`
       - Contains a list of all the guild's emojis.
    - features - `list[str]`
       - List of strings listing enabled guild features. 
    - mfa_level - `Literal["NONE","ELEVATED"]`
      - String literal indicating **M**ulti **F**actor **A**uthentication level to enter guild.
    - application_id - `Optional[discmoji.Snowflake]`
      - Contains the application's id if the guild is bot creates, else None.
    - system_channel_id - `Optional[discmoji.Snowflake]`
      - Contains the system channel's id, if exists.
    - system_channel_flags - `list[dict[str,int]]`
      - A list of all enabled system channel flags.
      - key is always capital ( [see ddev documentation](https://discord.com/developers/docs/resources/guild#guild-object-system-channel-flags) ), value is always an integer.
    - rules_channel_id - `Optional[discmoji.Snowflake]`
      - The rule channel's id, if exists.
       """
    def __init__(self,_data: dict[str, str | int | dict | None]):
        self.id = Snowflake(_data["id"])
        self.name: str = _data["name"]
        self.icon: str = f"https://cdn.discordapp.com/icons/{self.id}/{_data["avatar"]}.{"gif" if _data["avatar"].startswith("a_") else "png"}"
        self.splash: str = f"https://cdn.discordapp.com/splashes/{self.id}/{_data["splash"]}.{"gif" if _data["avatar"].startswith("a_") else "png"}"
        self.discovery_splash: Optional[str] = f"https://cdn.discordapp.com/discovery-splashes/{self.id}/{_data.get("discovery_splash")}.{"gif" if _data.get("discovery_splash").startswith("a_") else "png"}" if _data.get("discovery_splash") is not None else None
        self.owner: Optional[bool] = _data.get("owner")
        self.owner_id: Snowflake = Snowflake(_data["owner_id"])
        self.permissions: Optional[str] = _data.get("permissions")
        self.afk_channel_id: Optional[Snowflake] = Snowflake(_data.get("afk_channel_id")) if _data.get("afk_channel_id") is not None else None
        self.afk_timeout: int = _data["afk_timeout"]
        self.widget_enabled: Optional[bool] = _data.get("widget_enabled")
        self.widget_channel_id: Optional[Snowflake] = Snowflake(_data.get("widget_channel_id")) if _data.get("widget_channel_id") is not None else None
        self.verification_level: dict[str,int] = _find_verification_level(VerificationLevels,_data["verification_level"])
        self.default_msg_notifs: dict[str,int] = _find_notif_level(DefaultMessageNotifLevel,_data["default_message_notifications"])
        self.explicit_filter_lvl: dict[str,int] = _find_expl_level(ExplicitContentFilter,_data["explicit_content_filter"])
        self.roles: list[Role] = [Role(role) for role in _data["roles"]]
        self.emojis: list[Emoji] = [Emoji(emoji) for emoji in _data["emoji"]]
        self.features: list[str] = _data["features"]
        self.mfa_level = "NONE" if _data["mfa_level"] == 0 else "ELEVATED"
        self.application_id: Optional[Snowflake] = Snowflake(_data["application_id"]) if _data.get("application_id") is not None else None
        self.system_channel_id: Optional[Snowflake] = Snowflake(_data["system_channel_id"]) if _data.get("system_channel_id") is not None else None
        self.system_channel_flags: list[dict[str,int]] = _get_system_flags(_data["system_channel_flags"],SystemChannelFlags)
        self.rules_channel_id: Optional[Snowflake] = Snowflake(_data["rules_channel_id"]) if _data.get("rules_channel_id") is not None else None
        ...
        