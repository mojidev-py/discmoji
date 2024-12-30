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
import aiohttp
import websockets
import json
from enum import Enum, IntEnum
from typing import Any, Literal,Optional,Self
from .snowflake import Snowflake
import enum
from .exceptions import InternalDiscmojiException
import logging
import sys
import colorama

class RequestBody:
    def __init__(self,response: aiohttp.ClientResponse):
        self.headers = response.headers
        self.data: dict = json.loads(response.content.read_nowait().decode())
        self.status = response.status


class WebsocketPayload:
    def __init__(self,response: Optional[websockets.Data],opcode: int ,data: dict | int | None):
        self.__serialized: dict = json.loads(response) if response else None
        self.opcode = self.__serialized.get("op") if self.__serialized else opcode
        self.data = self.__serialized.get("d") if self.__serialized else data
        self.seq = self.__serialized.get("s") if self.__serialized else None
        self.event = self.__serialized.get("t") if self.__serialized else None
    
    def jsonize(self) -> str:
        if isinstance(self.data,dict) and self.opcode not in range(0,31):
            data = {
                "op": 0,
                "d": self.data
            }
            # type: ignore
            return json.dumps(data)
        elif isinstance(self.data, dict) and self.opcode in range(0,31):
            data = {
                "op": self.opcode,
                "d": self.data
            }            
            # type: ignore
            return json.dumps(data)
    
class Locales(Enum):
    ID = "Indonesian"
    DA = "Danish"
    DE = "German"
    EN_GB = "UK English"
    EN_US = "US English"
    ES_ES = "Spanish"
    ES_419 = "Spanish, LATAM"
    FR = "French"
    HR = "Croatian"
    IT = "Italian"
    LT = "Lithuanian"
    HU = "Hungarian"
    NL = "Dutch"
    NO = "Norwegian"
    PL = "Polish"
    PT_BR = "Portuguese, Brazilian"
    RO = "Romanian"
    FI = "Finnish"
    SV_SE = "Swedish"
    VI = "Vietnamese"
    TR = "Turkish"
    CS = "Czech"
    EL = "Greek"
    BG = "Bulgarian"
    RU = "Russian"
    UK = "Ukrainian"
    HI = "Hindi"
    TH = "Thai"
    ZH_CN = "Chinese"
    JA = "Japanese"	
    ZH_TW = "Chinese, Taiwan"
    KO = "Korean"

class UserFlags(IntEnum):
    STAFF = 1 << 0
    PARTNER = 1 << 1
    HYPESQUAD = 1 << 2 
    BUG_HUNTER_1 = 1 << 3
    HOUSE_BRAVERY = 1 << 6
    HOUSE_BRILLIANCE = 1 << 7
    HOUSE_BALANCE = 1 << 8
    PREMIUM_EARLY_SUPPORTER = 1 << 9
    TEAM_PSEUDO_USER = 1 << 10
    BUG_HUNTER_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    VERIFIED_DEV = 1 << 17
    CERTIFIED_MOD = 1 << 18
    BOT_ONLY_HTTP = 1 << 19
    ACTIVE_DEV = 1 << 22

def _flags_parse(input: int) -> list[dict[str,int | Any]] | None:
    parsed = []
    if input == None:
        return
    bytesinput = bytes(input)
    for key,value in UserFlags.__members__.items():
        for num in bytesinput:
            if bytes(num) == value:
              parsed.append({key:value})
    return parsed

def _return_nitro_type(data: int) -> Literal["Nitro Classic","Nitro","Nitro Basic"] | None:
    if data == 0:
        return None
    if data == 1:
        return "Nitro Classic"
    if data == 2:
        return "Nitro"
    if data == 3:
        return "Nitro Basic"

class VerificationLevels(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4
    
def _find_verification_level(input: int):
    for key,value in VerificationLevels.__members__.items():
        if value == input:
            return {key:value}

class DefaultMessageNotifLevel(Enum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1

def _find_notif_level(input: int):
    for key, value in DefaultMessageNotifLevel.__members__.items():
        if value == input:
            return {key:value}

class ExplicitContentFilter(Enum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2

def _find_expl_level(input: int):
    for key, value in ExplicitContentFilter.__members__.items():
        if value == input:
            return {key:value}

class RoleTags:
    """Role metadata object.
    ## Attributes
    - bot_id - `Optional[discmoji.Snowflake]`
       - Snowflake representing the id of the bot associated with this role, can be None.
    - integration_id - `Optional[discmoji.Snowflake]`
       - Snowflake representing the id of the integration associated with this role, can be None.
    - premium_role - `Optional[bool]`
       - Indicates whether this is a booster role or not. (role given when boosting)
    - subscription_sku_listing - `Optional[discmoji.Snowflake]`
       - The id of this role's subscription SKU and listing, may be None.
    - available_for_purchase - `Optional[bool]`
       - Whether this role is a purchaseable role e.g whether this role is a role awarded through guild membership.
    - guild_connections - `Optional[bool]`
       - Whether this role is a guild's linked role."""
    def __init__(self,_data: dict):
        self.bot_id: Optional[Snowflake] = Snowflake(_data["bot_id"]) if _data.get("bot_id") is not None else None
        self.integration_id: Optional[Snowflake] = Snowflake(_data["integration_id"]) if _data.get("integration_id") is not None else None
        self.premium_role: Optional[bool] = _data.get("premium_subscriber") 
        self.subscription_sku_listing: Optional[Snowflake] = Snowflake(_data["subscription_listing_id"]) if _data.get("bot_id") is not None else None
        self.available_for_purchase: Optional[bool] = _data.get("available_for_purchase")
        self.guild_linked_role: Optional[bool] = _data.get("guild_linked_role")

class PermissionsBits(enum.IntFlag):
    """Enum used by permissions related functions to create or check permissions.
    Use this permissions enum with bitwise operators, like such:
    ```
    permissions = PermissionsBits.create_invites | PermissionsBits.kick_members | ...
    ```
    These are different from intents, do not mix them up. \n
    `|` - adds a permission \n
    `&` - checks if object that is applicable has that permission \n
    `~` -  checks if object that is applicable does NOT have that permission \n
    use these operators as such:
    ```python
    (perms & Permissions.create_invites) == 1 # true
    perms = PermissionsBits.Example | Permissions.OtherExample # 2304 (example, not accurate)
    ~PermissionsBits.LALALA == 21030 # true (example, not accurate)
    ```
    It is advised to use permission check/creator functions to do this work for you, since this may not work as expected.
    """
    create_invites = 1 << 0
    kick_members = 1 << 1
    ban_members = 1 << 2
    admin = 1 << 3
    manage_channels = 1 << 4
    manage_guild = 1 << 5
    reactions = 1 << 6
    audit_log = 1 << 7
    priority_speaker = 1 << 8
    stream = 1 << 9
    view_channel = 1 << 10
    send_messages = 1 << 11
    tts_messages = 1 << 12 
    manage_messages = 1 << 13
    embed_links = 1 << 14
    attach_files = 1 << 15
    read_message_history = 1 << 16 
    mention_everyone = 1 << 17
    external_emojis = 1 << 18
    guild_insights = 1 << 19
    connect = 1 << 20
    speak = 1 << 21
    mute_members = 1 << 22
    deafen_members = 1 << 23
    move_members = 1 << 24
    use_vad = 1 << 25
    change_nickname = 1 << 26
    manage_nicknames = 1 << 27
    manage_roles = 1 << 28
    manage_webhooks = 1 << 29
    guild_expressions = 1 << 30
    use_app_cmds = 1 << 31
    req_to_speak = 1 << 32
    events = 1 << 33
    threads = 1 << 34
    public_threads = 1 << 35
    private_threads = 1 << 36
    use_external_stickers = 1 << 37
    send_messages_threads = 1 << 38
    embedded_activities = 1 << 39
    moderate_members = 1 << 40
    creator_monetization_analytics = 1 << 41
    soundboard = 1 << 42
    external_sounds = 1 << 45
    voice_messages = 1 << 46
    polls = 1 << 49
    external_apps = 1 << 50
    

class Permissions:
    """Contains the result of functions that return permissions. 
    These classes can be used to create new permissions, through 'flipping' each one of the attributes. (e.g False to True)
    This provides a more abstracted interface to creating and checking permissions, than `discmoji.PermissionsBits`."""
    def __init__(self):
        self.create_invites = False
        """Creating invites"""
        self.kick_members = False
        """kicking members"""
        self.ban_members = False
        """banning members"""
        self.admin = False
        """administrator perms"""
        self.manage_channels = False
        """managing channels e.g deleting them, moving them"""
        self.manage_guilds = False
        """managing guilds e.g changing guild banner etc."""
        self.reactions = False
        """reaction related permissions"""
        self.audit_log = False
        """Viewing audit log events"""
        self.priority_speaker = False
        """Priority speaker in voice chats"""
        self.stream = False
        """Stream in voice chats"""
        self.view_channel = False
        """Viewing specific channel"""
        self.send_messages = False
        """Pretty self explanatory"""
        self.tts_messages = False
        """TTS messages, TTS standing for **T**ext **T**o **S**peech"""
        self.manage_messages = False
        """Allows you to delete messages"""
        self.embed_links = False
        """Allows links to automatically be embedded"""
        self.attach_files = False
        """Pretty self-explanatory here."""
        self.message_history = False
        """Message history"""
        self.everyone = False
        """Permission that allows you to mention everyone"""
        self.external_emojis = False
        """Allows you to use emojis from other servers that have been joined, if Nitro user."""
        self.insights = False
        """Allows you to view guild insights"""
        self.connect = False
        """Connecting in a VC (**V**oice **C**hannel)"""
        self.speak = False
        """Speaking in a VC"""
        self.mute_members = False
        """Muting members"""
        self.deafen_members = False
        """Deafening members in a VC"""
        self.move_members = False
        """Moving members to other channels"""
        self.use_vad = False
        """Allowing user in VC to use VAD. (**V**oice **A**ctivity **D**etection)"""
        self.change_nickname = False
        """Allows user to change own nickname"""
        self.manage_nicknames = False
        """Allows user to manage other user's nicknames"""
        self.manage_roles = False
        """Allows user to manage guild's roles."""
        self.manage_webhooks = False
        """Allows user to configure webhooks"""
        self.guild_expressions = False
        """Allows user to edit and delete guild stickers or emojis"""
        self.use_app_cmds = False
        """Allows user to use external application commands"""
        self.req_to_speak = False
        """Allows user to request to speak in a Stage channel"""
        self.events = False
        """Allows for deleting and scheduling events for discord servers."""
        self.threads = False
        """Allows for managing of threads"""
        self.public_threads = False
        """Allows user to create public threads"""
        self.private_threads = False
        """Allows user to create private threads"""
        self.external_stickers = False
        """Allows user to use stickers from other servers."""
        self.messages_in_threads = False
        """Allows user to send messages in threads"""
        self.embedded_activities = False
        """Allows for using activities"""
        self.moderate_members = False
        """Allows user to time out other users"""
        self.creator_monetization_analytics = False
        """Allows user to view role subscription insights."""
        self.soundboard = False
        """Usage of soundboard."""
        self.external_sounds = False
        """Usage of external sounds from other guilds."""
        self.voice_messages = False
        """Allowing of user to send voice messages."""
        self.polls = False
        """Allowing of user to create polls"""
        self.external_apps = False
        """Allows user to use external apps."""
        
    @classmethod
    def _convert_perms(cls,input: int) -> Self:
            """Internal method used to configure base permissions to liking."""
            return_class = cls()
            bytes_input = bytes(input)
            for key,item in PermissionsBits.__members__.items():
                if bytes_input & bytes(item) == True:
                    try:    
                        setattr(return_class,key,True)
                    except AttributeError as e:
                        raise InternalDiscmojiException(e.args)
            return return_class
    
    
    def _deconv_perms(self) -> int:
        """An internal utility function that turns the Permissions object back into an integer. """
        integer = 0
        for item,value in self.__dict__.items():
            if type(value) == function:
                continue
            else:
                if value:
                    integer += PermissionsBits.__members__[item]
        return integer
class SystemChannelFlags(Enum):
    SUPPRESS_JOIN_NOTIFS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5

def _get_system_flags(input: int):
    byte_input = bytes(input)
    value_list = []
    for key,value in SystemChannelFlags.__members__.items():
        if byte_input & bytes(value):
            value_list.append({key:value})
    return value_list


def _get_nitro_rank(input: int):
    if input == 0:
        return None
    if input == 1:
        return "Tier 1"
    if input == 2:
        return "Tier 2"
    if input == 3:
        return "Tier 3"

logger = logging.getLogger("discmoji")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter(f"{colorama.Fore.RED}%(name)s {colorama.Fore.BLUE}%(levelname)s{colorama.Fore.RESET} at %(asctime)s: %(message)s",datefmt="%I:%M"))
logger.addHandler(ch)

def find_sticker_format_type(inp: int):
    if inp == 1:
        return "PNG"
    if inp == 2:
        return "APNG"
    if inp == 3:
        return "LOTTIE"
    if inp == 4:
        return "GIF"


class Opcodes(Enum):
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILD_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    ACK = 11
    REQ_SOUNDBOARD_SOUNDS = 31


class IntentsBits(enum.IntFlag):
    """A less abstracted interface than `discmoji.BotIntents` for making intents.
    This enum is meant to be used with bitwise operators. \n
    -| - adds an intent \n
    & - checks if bot has that intent \n
    ~ - checks if bot does not have that intent \n
    ```python
    # examples
    perms = IntentsBits.Example | IntentsBits.OtherExample
    (perms & IntentsBits.OtherExample) == True # true
    ~perms == 0 # true
    ```
    Note that this returns an integer, not a BotIntents class.
    """
    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_MODERATION = 1 << 2
    GUILD_EXPRESSIONS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DM = 1 << 12
    DM_REACTIONS = 1 << 13
    DM_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTOMOD_CONFIG = 1 << 20
    AUTOMOD_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DM_POLLS = 1 << 25

class ChannelFlags(enum.IntFlag):
    PINNED = 1 << 1
    REQUIRE_TAG = 1 << 4
    HIDE_MEDIA_DOWNLOAD_OPTIONS = 1 << 15
    

def _get_channel_flags(inp: int):
    byteinp = bytes(inp)
    returns = []
    for item,value in ChannelFlags.__members__.items():
        if byteinp & bytes(value):
            returns.append(item)
    return returns


class ForumTag:
    """Represents a tag that is able to be applied to a thread in a forum or media channel.
    ## Attributes
    - id - `discmoji.Snowflake`
      - The id of the tag.
    - name - `str`
      - the name of the tag.
    - moderated - `bool`
      - Whether this tag has to be added by a user with the `MANAGE_THREAD` permission or not.
    - emoji_id - `Optional[Snowflake]`
      - The id of the emoji that's on the tag (if exists)
    - emoji_name - `Optional[str]`
      - The name of the emoji that's on the tag (if exists)"""
    def __init__(self,_data: dict) -> None:
        self.id: Snowflake = Snowflake(_data["id"])
        self.name: str = _data["name"]
        self.moderated: bool = _data["moderated"]
        self.emoji_id: Optional[Snowflake] = Snowflake(_data["emoji_id"]) if _data.get("emoji_id") is not None else None
        self.emoji_name: Optional[str] = _data["emoji_name"] if _data.get("emoji_name") else None

class AppInfo:
    """Represents extra metadata associated with your application."""
    def __init__(self,_data: dict):
        pass

class MessageTypes(enum.IntFlag):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTOMOD_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44
    POLL_RESULT = 46

def find_message_type(input: int):
    for key in MessageTypes.__members__:
        if input == MessageTypes.__members__[key]:
            return key.lower().capitalize().replace("_"," ")

class MessageFlags(Enum):
    CROSSPOSTED =1 << 0	
    IS_CROSSPOST = 1 << 1	
    SUPPRESS_EMBEDS = 1 << 2	
    SOURCE_MESSAGE_DELETED = 1 << 3	
    URGENT = 1 << 4	
    HAS_THREAD = 1 << 5	
    EPHEMERAL =	1 << 6	
    LOADING = 1 << 7	
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8	
    SUPPRESS_NOTIFICATIONS = 1 << 12	
    IS_VOICE_MESSAGE = 1 << 13

def get_msg_flags(input: int):
    returned = []
    n = 0
    for item,value in MessageFlags._member_map_.items():
        n += 1
        if input & value.value:
            returned.append(item.lower().capitalize().replace("_"," "))
    return returned