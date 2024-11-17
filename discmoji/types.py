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
import asyncio
import json
from enum import Enum, IntEnum
from typing import Any, Literal
from typing import Optional
from .snowflake import Snowflake

class RequestBody:
    def __init__(self,response: aiohttp.ClientResponse):
        self.headers = response.headers
        self.data = json.loads(asyncio.run(response.content.read()).decode())
        self.status = response.status


class WebsocketPayload:
    def __init__(self,response: Optional[websockets.Data],opcode: int,data: dict):
        self.__serialized: dict = json.loads(response)
        self.opcode = self.__serialized.get("op") if self.__serialized.get("op") else opcode
        self.data = self.__serialized.get("d") if self.__serialized.get("data") else data
        self.seq = self.__serialized.get("s")
        self.event = self.__serialized.get("t")
    
    def jsonize(self) -> str:
        if isinstance(self.data,dict) and self.opcode not in range(0,31):
            self.data['op'] = 0 # type: ignore
            return json.dumps(self.data)
        elif isinstance(self.data, dict) and self.opcode in range(0,31):
            self.data['op'] = self.opcode # type: ignore
            # type ignore because on my vscode it keeps complaining about an undefined variable ;(
            return json.dumps(self.data)
    
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

def _flags_parse(enum: UserFlags,input: int) -> list[dict[str,int | Any]] | None:
    parsed = []
    bytesinput = bytes(input)
    for key,value in enum.__dict__.items():
        for num in bytesinput:
            if bytes(num) == value:
              parsed.append({key:value})
    if input == None:
        return
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
    
def _find_verification_level(enum: VerificationLevels,input: int):
    for key,value in enum.__dict__.items():
        if value == input:
            return {key:value}

class DefaultMessageNotifLevel(Enum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1

def _find_notif_level(enum: DefaultMessageNotifLevel,input: int):
    for key, value in enum.__dict__.items():
        if value == input:
            return {key:value}

class ExplicitContentFilter(Enum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2

def _find_expl_level(enum: ExplicitContentFilter,input: int):
    for key, value in enum.__dict__.items():
        if value == input:
            return {key:value}

class RoleTags:
    """Role metadata object.
    ## Attributes
    - bot_id - `Optional[discmoji.Snowflake]`
       - Snowflake representing the id of the bot associated with this role, can be None.
    - integration_id - `Optional[discmoji.Snowlflake]`
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

class Permissions:
    """Internal enum used by permissions related functions to create or check permissions.
    Use this permissions enum with bitwise operators, like such:
    ```
    permissions = Permissions.create_invites | Permissions.kick_members | ...
    ```"""
    create_invites = 1 << 0
    kick_members = 1 << 1
    ban_members = 1 << 2
    admin = 1 << 3
    manage_channels = 1 << 4
    manage_guild = 1 << 5
    add_reactions = 1 << 6
    view_audit_log = 1 << 7
    priority_speaker = 1 << 8
    stream = 1 << 9
    view_channel = 1 << 10
    send_messages = 1 << 11
    

