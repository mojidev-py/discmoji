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
from ..user import User
import datetime
from ..guild_domain.roles import Role
from ..guild_domain.channel import Channel
from .attachment import Attachment
from .embed import Embed
from .reactions import Reaction
from .message_ref import MessageReference
from .._types import find_message_type,get_msg_flags

class Message:
    """Represents a discord message.
    ## Attributes
    - id - `discmoji.Snowflake`
      - The message's id.
    - channel_id - `discmoji.Snowflake`
      - The id of the channel this message came from.
    - author - `discmoji.User`
      - The user that made this message.
    - content - `str`
      - The content of this message. Will be `''` if you do not have the message content intent.
    - timestamp - `datetime.datetime`
      - A `datetime` object containing the time this message was made.
    - edit_time - `datetime.datetime | None`
      - A `datetime` object containing the time this message was edited, if it was.
    - tts - `bool`
      - Whether this message was a TTS one or not.
    - mentions_everyone - `bool`
      - Whether this message mentions everyone (`@everyone`)
    - mentions - `list[discmoji.User]`
      - The users this message mentions.
    - role_mentions - `list[discmoji.Role]`
      - The roles this message mentions.
    - channel_mentions - `list[discmoji.Channel] | None`
      - The channels this message mentions. Keep in mind that this will not contain all channel mentions, only those that are viewable to everyone in the guild.
    - attachments - `list[discmoji.Attachment]`
      - The attachments associated with this message.
    - embeds - `list[discmoji.Embed]`
      - The embeds with this message.
    - reactions - `list[discmoji.Reaction] | None`
      - The reactions that this message has.
    - pinned - `bool`
      - Whether this message is pinned in the channel or not.
    - webhook_id - `discmoji.Snowflake | None`
      - The id of the webhook this was sent from, if applicable.
    - type - `str`
      - The type of the message. (See Message Resource, discord documentation)
    - flags - `list[str]`
      - A list containing the flags this message has. (See message resource, discord docs)
    - message_ref - `discmoji.MessageReference | None`
      - Data about the source of the referenced message.
    - referenced - `discmoji.Message | None`
      - The message this message originated from.
    - thread - `discmoji.Channel | None`
      - The thread this message was made in."""
    def __init__(self,_dict: dict):
        self.id: Snowflake = Snowflake(_dict["id"])
        self.channel_id: Snowflake = Snowflake(_dict["channel_id"])
        self.author: User = User(_dict["author"]) if _dict.get("author") else None
        self.content: str = _dict["content"]
        self.timestamp = datetime.datetime.fromisoformat(_dict["timestamp"])
        self.edited_time = datetime.datetime.fromisoformat(_dict["edited_timestamp"]) if _dict.get("edited_timestamp") else None
        self.tts: bool = _dict["tts"]
        self.mentions_everyone: bool = _dict["mention_everyone"]
        self.mentions = [User(data) for data in _dict["mentions"]]
        self.role_mentions = [Role(data) for data in _dict["mention_roles"]]
        self.channel_mentions = [Channel(data) for data in _dict["mention_channels"]] if _dict.get("mention_channels") else None
        self.attachments = [Attachment(data) for data in _dict["attachments"]]
        self.embeds = [Embed(data) for data in _dict["embeds"]]
        self.reactions = [Reaction(data) for data in _dict["reactions"]] if _dict.get("reactions") else None
        self.pinned: bool = _dict["pinned"]
        self.webhook_id = Snowflake(_dict["webhook_id"]) if _dict.get("webhook_id") else None
        self.type = find_message_type(_dict["type"])
        self.flags = get_msg_flags(_dict["flags"])
        self.message_ref = MessageReference(_dict["message_reference"]) if _dict.get("message_reference") else None
        self.referenced = self(_dict["referenced_message"]) if _dict.get("referenced_message") else None
        self.thread = Channel(_dict["thread"]) if _dict.get("thread") else None
        self.position = _dict.get("position")
        