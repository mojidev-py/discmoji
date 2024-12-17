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

class WelcomeScreenChannel:
    """Represents a Welcome Screen's channels.
    ## Attributes
    - channel_id - `discmoji.Snowflake`
      - The channel id.
    - description - `str`
      - The description provided for this in the welcome screen.
    - emoji_id - `Optional[discmoji.Snowflake]`
      - The emoji id for this welcome screen channel's emoji, if it is custom.
    - emoji_name - `Optional[str]`
      - The name for the emoji if custom, the unicode emoji if standard, and null if no emoji is set."""
    def __init__(self,_data: dict):
        self.channel_id = Snowflake(_data["channel_id"])
        self.description: str = _data["description"]
        self.emoji_id: Optional[Snowflake] = _data.get("emoji_id")
        self.emoji_name: Optional[str] = _data.get("emoji_name")

class WelcomeScreen:
    """Represents a Guild's welcome screen.
    ## Attributes
    - description - `Optional[str]`
     - description for the server, shown in the welcome screen.
    - welcome_channels - `list[discmoji.WelcomeScreenChannel]`
     - List of `WelcomeScreenChannel`'s that are a part of this server's welcome screen."""
    def __init__(self,dict: dict):
        self.description: Optional[str] = dict.get("description")
        self.welcome_channels = [WelcomeScreenChannel(channel) for channel in dict["welcome_channels"]]
        