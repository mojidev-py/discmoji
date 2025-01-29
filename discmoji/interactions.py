"""Interactions"""
from .snowflake import Snowflake
from .guild_domain.guild import Guild
from .guild_domain.channel import Channel
from .guild_domain.guild_member import GuildMember
from .user import User
from .message_domain.message import Message

class Interaction:
    """Represents a slash command context interface."""
    def __init__(self,_data: dict):
        self.id = Snowflake(_data["id"])
        self.app_id = Snowflake(_data["application_id"])
        self._type = _data["type"]
        self.data = ...
        # placeholder for now because needs an object
        self.guild = Guild(_data.get("guild")) if _data.get("guild") else None
        self.channel = Channel(_data.get("channel")) if _data.get("channel") else None
        self.member = GuildMember(_data.get("member")) if _data.get("member") else None
        self.user = User(_data.get("user")) if _data.get("user") else None
        self._token = _data["token"]
        self.message = Message(_data["message"]) if _data.get("message") else None
        self.locale = _data["locale"]
        self.guild_locale = _data["guild_locale"]
        ...
        # it for now