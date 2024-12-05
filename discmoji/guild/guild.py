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
from typing import Optional,TypeAlias
from ..types import _find_verification_level,_find_notif_level,_find_expl_level,_get_system_flags,_get_nitro_rank,Locales
from .roles import Role
from .emoji import Emoji
from .welcomescreen import WelcomeScreen
from .sticker import Sticker
from ..exceptions import DiscmojiRetrievalError,Forbidden,UnknownHTTPError
from ..bot import Bot
from mappers.gp_mapper import GuildPreviewMapper
from .gp_payload import _GuildPreviewPayload
class Guild:
    """Represents a Guild/Server on Discord. 
    There is an alias for this called Server.
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
    - max_presences - `Optional[int]`
      - Almost always None, unless guild has a very sizable amount of members.
        - e.g Midjourney
    - max_members - `Optional[int]`
        - The maximum member threshold for the guild.
    - vanity_url_code - `Optional[str]`
        - The vanity url code for the guild.
    - description - `Optional[str]`
        - The description of the guild.
    - banner - `Optional[str]`
        - Contains a CDN link to the guild's banner. May be None.
    - premium_tier - `Literal["Tier 1","Tier 2","Tier 3"] | None`
        - The server boost rank of the guild.
    - premium_subscription_count - `int`
        - The amount of boosts this guild has.
    - preferred_locale - `str`
        - Returns the language for the locale this guild is in.
    - public_upd_channel_id - `Optional[discmoji.Snowflake]`
        - the public updates channel's id, if exists.
    - max_video_channel_users - `Optional[int]`
        - The maximum amount of users that can be inside a video channel.
    - max_stage_video_channel_users - `Optional[int]`
        - The maximum amount of users that can be inside a stage video channel.
    - approximate_member_count - `Optional[int]`
        - Only a non-None value if retrieved from the `Get Guild` endpoint with the `with_count` param.
    - approximate_presence_count - `Optional[int]`
        - Only a non-None value if retrieved from the `Get Guild` endpoint with the `with_count` param.
    - welcome_screen - `Optional[WelcomeScreen]`
        - The welcome screen for this guild, if exists.
    - stickers - `Optional[list[discmoji.Sticker]]`
        - A list of stickers for this guild.
    - progress_bar_enabled - `bool`
        - Whether the guild's boost progress bar is enabled.
    - safety_alerts_channel_id - `Optional[discmoji.Snowflake]`
        - The id of the safety alerts channel for this guild."""
    def __init__(self,_data: dict[str, str | int | dict | None | bool]):
        self.id = Snowflake(_data["id"])
        self.name: str = _data["name"]
        self.icon: str = f"https://cdn.discordapp.com/icons/{self.id}/{_data["icon"]}.{"gif" if _data["icon"].startswith("a_") else "png"}"
        self.splash: str = f"https://cdn.discordapp.com/splashes/{self.id}/{_data["splash"]}.{"gif" if _data["splash"].startswith("a_") else "png"}"
        self.discovery_splash: Optional[str] = f"https://cdn.discordapp.com/discovery-splashes/{self.id}/{_data.get("discovery_splash")}.{"gif" if _data.get("discovery_splash").startswith("a_") else "png"}" if _data.get("discovery_splash") is not None else None
        self.owner: Optional[bool] = _data.get("owner")
        self.owner_id: Snowflake = Snowflake(_data["owner_id"])
        self.permissions: Optional[str] = _data.get("permissions")
        self.afk_channel_id: Optional[Snowflake] = Snowflake(_data.get("afk_channel_id")) if _data.get("afk_channel_id") is not None else None
        self.afk_timeout: int = _data["afk_timeout"]
        self.widget_enabled: Optional[bool] = _data.get("widget_enabled")
        self.widget_channel_id: Optional[Snowflake] = Snowflake(_data.get("widget_channel_id")) if _data.get("widget_channel_id") is not None else None
        self.verification_level: dict[str,int] = _find_verification_level(_data["verification_level"])
        self.default_msg_notifs: dict[str,int] = _find_notif_level(_data["default_message_notifications"])
        self.explicit_filter_lvl: dict[str,int] = _find_expl_level(_data["explicit_content_filter"])
        self.roles: list[Role] = [Role(role) for role in _data["roles"]]
        self.emojis: list[Emoji] = [Emoji(emoji) for emoji in _data["emoji"]]
        self.features: list[str] = _data["features"]
        self.mfa_level = "NONE" if _data["mfa_level"] == 0 else "ELEVATED"
        self.application_id: Optional[Snowflake] = Snowflake(_data["application_id"]) if _data.get("application_id") is not None else None
        self.system_channel_id: Optional[Snowflake] = Snowflake(_data["system_channel_id"]) if _data.get("system_channel_id") is not None else None
        self.system_channel_flags: list[dict[str,int]] = _get_system_flags(_data["system_channel_flags"])
        self.rules_channel_id: Optional[Snowflake] = Snowflake(_data["rules_channel_id"]) if _data.get("rules_channel_id") is not None else None
        self.max_presences: Optional[int] = _data["max_presences"] if _data.get("max_presences") is not None else None
        self.max_members: Optional[int] = _data["max_members"] if _data.get("max_members") is not None else None
        self.vanity_url_code: Optional[str] = _data.get("vanity_url_code")
        self.description: Optional[str] = _data.get("description")
        self.banner: Optional[str] = f"https://cdn.discordapp.com/banners/{self.id}/{_data["banner"]}.{"gif" if _data["banner"].startswith("a_") else "png"}" if _data.get("banner") else None  
        self.premium_tier: str = _get_nitro_rank(_data["premium_tier"])
        self.premium_subscription_count: int = _data["premium_subscription_count"]
        self.preferred_locale: str = Locales.__members__[_data["preferred_locale"].upper().replace("-","_")]
        self.public_upd_channel_id: Optional[Snowflake] = Snowflake(_data["public_updates_channel_id"]) if _data.get("public_updates_channel_id") is not None else None
        self.max_video_channel_users: Optional[int] = _data.get("max_video_channel_users")
        self.max_stage_video_channel_users: Optional[int] = _data.get("max_stage_video_channel_users")
        self.approximate_member_count: Optional[int] = _data.get("approximate_member_count")
        self.approximate_presence_count: Optional[int] = _data.get("approximate_presence_count")
        self.welcome_screen: Optional[WelcomeScreen] = WelcomeScreen(_data["welcome_screen"]) if _data["welcome_screen"] is not None else None
        self.stickers: Optional[list[Sticker]] = [Sticker(sticker) for sticker in _data["stickers"] if _data.get("stickers")]
        self.progress_bar_enabled: bool = _data["premium_progress_bar_enabled"]
        self.safety_alerts_channel_id = _data["safety_alerts_channel_id"]


    async def get_own_preview(self,bot: Bot):
        """
        **Co-routine** \n
        Retrieves the current guild's community preview.
        ## Parameters
        - bot - `discmoji.Bot`
          - Needed for permissions when retrieving data. (This is a minor inconvenience as we develop through later versions)
        ## Returns
        - **discmoji.GuildPreview**
           - The guild's preview.
        
        ## Raises
        - **DiscmojiRetrievalError**
           - Failed to retrieve community preview."""
        req = await bot.__http.request("get",f"/guilds/{self.id}/preview")
        if req.status >= 400:
            raise DiscmojiRetrievalError("get_own_preview()","Unspecified error occured while trying to retrieve current guild's preview.")    
        else:
            content = GuildPreviewMapper(_GuildPreviewPayload(req)).map()
            return content
    
    
    async def edit_guild(self,bot: Bot,**kwargs):
        """**Co-routine** \n
        Allows you to edit the guild's settings. 
        ## Parameters
         - bot - `discmoji.Bot`
           - Needed for authentication.
         - kwargs - `Any`
           - The fields in the guild you want to change. Check documentation for possible fields. (must be keyword arguments)
        ## Returns
        - **Self/discmoji.Guild**
          - The guild with changed settings/fields
        ## Raises
        - **Forbidden**
          - The bot isn't allowed to change a field.
        - **UnknownHTTPError**
          - An unspecified error occured."""
        req = await bot.__http.request("patch",f"/guilds/{self.id}",kwargs=kwargs)
        #                                                          ^^^^^^^^^^^
        #                                                    Kinda weird, but will work
        if req.status == 403:
            raise Forbidden("Bot does not have permissions to edit field on current guild.")
        elif req.status >= 400:
            raise UnknownHTTPError(req.status,"Was not able to change a field on current guild.")
        else:
            for key,value in req.data.items():
                setattr(self,key,value)
            return self
            # returns self for good chaining
    
    
    async def delete_guild(self,bot: Bot):
        """*Dangerous Method* \n
        **Co-routine** \n
        Deletes the current guild. Beware, as this is **irreversible**. User must be owner.
        ## Parameters
        - bot - `discmoji.Bot`
          - Needed for authentication.
        ## Returns
        **None**
        ## Raises
        - **Forbidden**
          - User is not owner of the guild.
        - **UnknownHTTPError**
          - An unspecified error occured.
        """
        req = await bot.__http.request("delete",f"/guilds/{self.id}")
        if req.status == 204:
            return
        if req.status == 403:
            raise Forbidden("Bot is not owner of the guild.")
        if req.status >= 400:
            raise UnknownHTTPError(req.status, "Was not able to delete the guild.")
          
        
        
        
type Server = Guild