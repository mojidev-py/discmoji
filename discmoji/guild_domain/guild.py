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
from .._types import _find_verification_level,_find_notif_level,_find_expl_level,_get_system_flags,_get_nitro_rank,Locales
from .roles import Role
from .emoji import Emoji
from .welcomescreen import WelcomeScreen
from .sticker import Sticker
from ..exceptions import DiscmojiRetrievalError,Forbidden,UnknownHTTPError
from ..bot import Bot
from .mappers.gp_mapper import GuildPreviewMapper
from .gp_payload import _GuildPreviewPayload
from .channel import Channel
from .c_payload import _ChannelPayload
from .mappers.c_mapper import ChannelMapper
from .threadmember import ThreadMember
from .gm_payload import _GuildMemberPayload
from mappers.gm_mapper import GuildMemberMapper
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
        self.__channel_cache = []


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
        req = await bot.http.request("get",f"guilds/{self.id}/preview")
        if req.status >= 400:
            raise DiscmojiRetrievalError(f"get_own_preview(bot: {bot})","Unspecified error occured while trying to retrieve current guild's preview.")    
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
        req = await bot.http.request("patch",f"guilds/{self.id}",kwargs=kwargs)
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
        req = await bot.http.request("delete",f"guilds/{self.id}")
        if req.status == 204:
            return
        if req.status == 403:
            raise Forbidden("Bot is not owner of the guild.")
        if req.status >= 400:
            raise UnknownHTTPError(req.status, "Was not able to delete the guild.")

    async def channels(self,bot: Bot):
      """
      **Co-routine** \n
      Returns the channels of the current guild.
      ## Parameters
      - bot - `discmoji.Bot`
         - Needed for authentication.
      
      ## Returns
      - `list[discmoji.Channel]`
        - A list of all the channels in the guild.
      ## Raises
      - **DiscmojiRetrievalError**
        - An unspecified error occured."""
      req = await bot.http.request("get",f"guilds/{self.id}/channels")
      if req.status == 200:
        self.__channel_cache = [Channel(channel) for channel in req.data]
        return [Channel(channel) for channel in req.data]
        # raw data is sent into Channel since it's convenient and more readable
        # and won't cause any problems in the future
      else:
        raise DiscmojiRetrievalError(f"channels(bot: {bot})","Could not retrieve guild channels.")
    
    async def create_channel(self,bot: Bot,**kwargs):
      """
      **Co-routine** \n
      Creates a channel in the current guild.
      
      ## Parameters
      - bot - `discmoji.Bot`
        - Needed for authentication.
      - kwargs - `Any`
        - Fields you want to specify for the new channel.
      
      ## Returns
      **discmoji.Channel**
        - The new channel
      
      ## Raises
      **UnknownHTTPError**
        - An unspecified error occured.      
      """
      formatted_kwargs = []
      for value in kwargs.values():
        if value is not int | str | Snowflake | bool | dict:
          formatted_kwargs.append(value.__dict__)
        else:
          formatted_kwargs.append(value)
      req = await bot.http.request("post",f"guilds/{self.id}/channels",kwargs=kwargs)
      if req.status <= 400:
        return ChannelMapper(_ChannelPayload(req.data)).map()
      else:
        raise UnknownHTTPError(req.status,"Failed to create channel.")
    
    async def modify_channel_position(self,bot: Bot,**kwargs):
      """Co-routine \n
      Modifies the provided channel's position on the guild's channel listing.
      
      ## Parameters
      - bot - `discmoji.Bot`
        - Needed for authentication.
      - kwargs - `Any`
        - Any keyword arguments that align with the field's name you want to change.
      
      ## Returns
      None
      
      ## Raises
      - UnknownHttpError
        - An unspecified error occurred."""
      req = await bot.http.request("patch",f"guilds/{self.id}/channels",kwargs=kwargs)
      if req.status >= 400:
        raise UnknownHTTPError(req.status,"Failed to update channel position.")
    
    async def active_guild_threads(self,bot: Bot,with_thread_members: bool = False):
      """Co-routine \n
      Lists the active guild thread channels, with the members that chatted in them, if enabled.
      
      ## Parameters
      - bot - `discmoji.Bot`
        - Needed for authentication.
      - with_thread_members - `bool = False`
        - Specifies whether you want to get the thread members in that channel, or not. Defaults to false.
      
      ## Returns
      - `list[discmoji.Channel]`
        - The active guild threads.
      - `tuple[list[discmoji.Channel | discmoji.ThreadMember]]`
        - A tuple, containing 2 lists that contain the active guild threads, and the thread members respectively if enabled."""
      req = await bot.__http.request("get",f"guilds/{self.id}/threads/active")
      if not with_thread_members:
        return [Channel(channel) for channel in req.data["threads"]]
      else:
        return [Channel(channel) for channel in req.data["threads"]],[ThreadMember(member) for member in req.data["members"]]
        # raw because it's easier ig
      
    
    async def get_member(self,bot: Bot,id: int):
      """Co-routine \n
      Retrieves a member from the guild.
      
      ## Parameters
      - id - `int`
        - The id of the member you want to retrieve.
      
      ## Returns
      - `discmoji.Member`
        - The member you requested.
      
      ## Raises
      - **DiscmojiRetrievalError**
        - An unspecified error occurred."""
      req = await bot.http.request("get",f"guilds/{self.id}/members/{id}")
      if req.status == 200:
        return GuildMemberMapper(_GuildMemberPayload(req.data)).map()
      else:
        raise DiscmojiRetrievalError(f"get_member(id: {id})","Could not retrieve member.")
    
    
    @classmethod
    async def get_guild(cls,bot: Bot,id: int):
        """ co-routine \n
        Retrieves a guild from its ID.
        ## Returns
        `discmoji.Guild` \n
        Success result.
        ## Raises
        `discmoji.UnknownHTTPError` \n
        Failed to retrieve guild.
        """
        rq = await bot.http.request('get',f'guilds/{id}')
        if rq.status >= 400:
            raise UnknownHTTPError(rq.status,"Failed to retrieve guild.")
        return cls(rq.data)

type Server = Guild 