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
from .overwrites import PermissionOverwrite
from datetime import datetime
from ..types import _get_channel_flags
class Channel:
    """Represents a text channel. Also the base class which all other Channel classes inherit from.
    ## Attributes
    - id - `discmoji.Snowflake`
      - ID of the channel.
    - guild_id - `Optional[discmoji.Snowflake]`
      - The ID of the guild this channel came from. May be none in some gateway payloads.
    - position - `Optional[int]`
      - The position of the channel in the guild's channel listing. May be none.
    - overwrites - `Optional[list[PermissionOverwrite]]`
      - A list of permission overwrites for this channel.
    - name - `Optional[str]`
      - The name of the channel.
    - topic - `Optional[str]`
      - Topic of this channel.
    - last_message_id - `Optional[discmoji.Snowflake]`
      - The last message in this channel's id, if exists.
    - rate_limit_per_user - `Optional[int]`
      - The slowmode (in seconds) for this channel, if applicable.
    - parent_id -  `Optional[discmoji.Snowflake]`
      - The category in which this channel is in if it's a guild and the text channel this thread was created if it's a thread.
    - last_pin_date - `Optional[datetime.datetime]`
      - A `datetime` object showing when the last message was pinned to this channel's pinboard, if any.
    - flags - `list`
      - A list of the names of the flags this channel has."""
    def __init__(self,_data: dict):
        self.id: Snowflake = Snowflake(_data["id"])
        self.guild_id: Optional[Snowflake] = Snowflake(_data["guild_id"]) if _data.get("guild_id") is not None else None
        self.position: Optional[int] = _data.get("position")
        self.overwrites: Optional[list[PermissionOverwrite]] = [PermissionOverwrite(overwrite) for overwrite in _data["permission_overwrites"]] if _data.get("permission_overwrites") else None
        self.name: Optional[str] = _data.get("name")
        self.topic: Optional[str] = _data.get("topic")
        self.last_message_id: Optional[Snowflake] = Snowflake(_data["last_message_id"]) if _data.get("last_message_id") is not None else None
        self.rate_limit_per_user: Optional[int] = _data.get("rate_limit_per_user")
        self.parent_id: Optional[Snowflake] = Snowflake(_data["parent_id"]) if _data.get("parent_id") is not None else None
        self.last_pin_date: Optional[datetime] = datetime.fromisoformat(_data["last_pin_timestamp"]) if _data.get("last_pin_timestamp") else None
        self.flags = _get_channel_flags()