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
SOFTWARE."""

from enum import Enum
from typing import *
import json
import logging
from colorama import Fore, Style
from .guild import Guild
from .user import User

initiatelogging = logging.getLogger("discmoji")
formatter = logging.Formatter(fmt=Style.BRIGHT+"[%(name)s-%(levelname)s-%(asctime)s]:%(message)s",datefmt="at %H:%M:%S")

class OPCODES(Enum):
    # internal class that's used for getting opcodes easily without typing the code in manually
    IDENTIFY = 0
    RESUME = 6
    HEARTBEAT = 1
    REQUEST_GUILD_MEMBERS = 8
    UPDATE_VOICE_STATE = 4
    PRESENCE_UPDATE = 3
    HELLO = 10
    RECONNECT = 7
    INVALID = 9
    EVENT = 0
    ACK = 11
    HTTP = None




class Payload:
    def __init__(self,
                 code: int | None,
                 d: Optional[Dict | str | int],
                 event_name: Optional[str],
                 s: Optional[int]):
        # class used for representing a payload from the api, or to the api
        # event_name attribute handles the event name from the gateway that GatewayManager handles 
        self.code = code
        self.event_name = event_name
        self.data = d
        self.seq = s
        
    def jsonize(self):
        # jsonizes the payload to be sent (websockets lib restrictions)
        jsoned = {
            "op": self.code,
            "d": self.data,
        }
        return json.dumps(jsoned)


class AppInfo:
    """A class that represents the application itself.
    Do not initialize this class. It will be initialized for you at bot connection."""
    def __init__(self,_data: Optional[Dict]):
        self.id = int(_data["id"])
        self.name: str = _data["name"]
        self.icon: str = _data["icon_hash"]
        self.desc: str = _data["description"]
        self.rpc_origins: Optional[List[str]] = _data["rpc_origins"]
        self.public: bool = _data["bot_public"]
        self.code_grant: bool = _data["bot_require_code_grant"]
        # placeholder till i get User object done
        self.bot: None = None
        self.tos_url: str = _data["terms_of_service_url"]
        self.privacy_policy_url: str = _data["privacy_policy_url"]
        # user object!!!!!
        self.owner: None = None
        # TEAMMMMMMM
        self.team: None = None
        self.guild_id = int(_data["guild_id"])
        self.guild: Guild = Guild(_data["guild"])
        self.cover_image: str = _data["cover_image"]
        self.flags: int = _data["flags"]
        self.approx_guild_count: int = _data["approximate_guild_count"]
        self.approx_user_installs: int = _data["approximate_user_install_count"]
        self.redirects: List[str] = _data["redirect_uris"]
        # more will be added

class PermissionsBits(Enum):
    CREATE_INSTANT_INVITE = 1 << 0 
    KICK_MEMBERS = 1 << 1
    BAN_MEMBERS = 1 << 2
    ADMINISTRATOR = 1 << 3
    MANAGE_CHANNELS = 1 << 4
    MANAGE_GUILD = 1 << 5
    ADD_REACTIONS = 1 << 6
    VIEW_AUDITS = 1 << 7
    PRIORITY_SPEAKER = 1 << 8
    STREAM = 1 << 9
    VIEW_CHANNEL = 1 << 10
    SEND_MESSAGES = 1 << 11
    TTS_MESSAGES = 1 << 12
    MANAGE_MESSAGES = 1 << 13
    EMBED_LINKS = 1 << 14
    ATTACH_FILES  = 1 << 15
    READ_MESSAGE_HISTORY = 1 << 16
    MENTION_EVERYONE = 1 << 17
    EXTERNAL_EMOJIS = 1 << 18
    VIEW_GUILD_INSIGHTS = 1 << 19
    CONNECT_VOICE = 1 << 20
    SPEAK_VOICE = 1 << 21
    MUTE_MEMBERS = 1 << 22
    DEAFEN_MEMBERS = 1 << 23
    MOVE_MEMBERS = 1 << 24
    USE_VAD = 1 << 25
    CHANGE_NICK = 1 << 26
    MANAGE_NICKS = 1 << 27
    MANAGE_ROLES = 1 << 28
    MANAGE_WEBHOOKS = 1 << 29
    GUILD_EXPRESSIONS = 1 << 30
    APPLICATION_CMDS = 1 << 31
    REQ_TO_SPEAK = 1 << 32
    MANAGE_EVENTS = 1 << 33
    MANAGE_THREADS = 1 << 34
    PUBLIC_THREADS = 1 << 35
    PRIVATE_THREADS = 1 << 36
    EXTERNAL_STICKERS = 1 << 37
    MSG_IN_THREAD = 1 << 38
    EMBEDDED_ACTIVITIES = 1 << 39
    MODERATE_MEMBERS = 1 << 40
    MONETIZATION_ANALYTICS = 1 << 41
    SOUNDBOARD = 1 << 42
    CREATE_GUILD_EXPRESSIONS = 1 << 43
    CREATE_EVENTS = 1 << 44
    USE_EXTERNAL_SOUNDS = 1 << 45
    SEND_VOICE_MESSAGES = 1 << 46
    SEND_POLLS = 1 << 49
    EXTERNAL_APPS = 1 << 50
    
class RoleTags:
    """Contains extra metadata about the role."""
    def __init__(self,_data: dict | None):
        self.bot_id: int = int(_data["bot_id"])
        self.integration_id: int = int(_data["integration_id"])
        self.premium: bool = True if _data["premium_subscriber"] is None else False
        self.available_for_purchase: bool = True if _data["available_for_purchase"] is None else False
        self.guild_connection: bool = True if _data["guild_connections"] is None else False

        

class File:
    def __init__(self,filename: str,filenames: list[str],__fileindex: int):
        self.filename = filename
        self.filenames = filenames
        self.__fileindex = __fileindex
        
class TEAMMEMBERSHIPSTATE(Enum):
    INVITED = 1
    ACCEPTED = 2
class TeamRole(Enum):
    OWNER = None
    ADMIN = "admin"
    DEV = "developer"
    VIEWER = "read_only"
class TeamMember:
    def __init__(self,_data: dict):
        self.membership_state: TEAMMEMBERSHIPSTATE.ACCEPTED | TEAMMEMBERSHIPSTATE.INVITED = _data.get("membership_state")
        self.team_id: int = _data.get("team_id")
        self.user: User = User(_data.get("user"))
        self.role: TeamRole.ADMIN | TeamRole.DEV | TeamRole.VIEWER = _data.get("role")
        





            
    
    
    
    