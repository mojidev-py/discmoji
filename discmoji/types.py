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

        
            