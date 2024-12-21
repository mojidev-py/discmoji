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

class MessageReference:
    """Represents a message reference."""
    def __init__(self,_dict: dict):
        self.type = "Default" if _dict.get("type") == 0 else "Forward" if _dict.get("type") else None
        self.orig_msg_id = Snowflake(_dict["message_id"]) if _dict.get("message_id") else None
        self.channel_id = Snowflake(_dict["channel_id"]) if _dict.get("channel_id") else None
        self.guild_id = Snowflake(_dict["guild_id"]) if _dict.get("guild_id") else None
        self.fail_if_not_exists: bool | None = _dict.get("fail_if_not_exists")