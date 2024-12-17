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
from .._types import find_sticker_format_type
from ..user import User
class Sticker:
    """Represents a discord Sticker.
    ## Attributes
    - id - `discmoji.Snowflake`
      - The id of the sticker.
    - pack_id - `discmoji.Snowflake`
      - The id of the pack this sticker came from, if it's a standard sticker.
    - name - `str`
      - The sticker's name.
    - description - `str`
      - The description of the sticker.
    - type - `Literal["STANDARD","GUILD"]`
      - Whether the sticker is part of the guild or is a standard one.
    - format_type - `Literal["PNG","APNG","GIF","LOTTIE"]`
      - The format type of the sticker.
    - available - `Optional[bool]`
      - Whether this guild sticker can be used. May be False due to loss of guild boosts. Can be none.
    - guild_id - `Optional[discmoji.Snowflake]`
      - The id of the guild this sticker came from. Can be none.
    - user - `Optional[discmoji.User]`
      - The user that made this guild sticker. Can be none.
    - sort_value - `Optional[int]`
      - The standard sticker's sort order within a pack.
    """
    def __init__(self,_data: dict):
        self.id = Snowflake(_data["id"])
        self.pack_id: Optional[Snowflake] = Snowflake(_data["pack_id"]) if _data.get("pack_id") else None
        self.name: str = _data["name"]
        self.description: str = _data["description"]
        self.type = "STANDARD" if _data["type"] == 1 else "GUILD"
        self.format_type = find_sticker_format_type(_data["type"])
        self.available: Optional[bool] = _data.get("available")
        self.guild_id: Optional[Snowflake] = Snowflake(_data["guild_id"]) if _data.get("guild_id") else None
        self.user: User = User(_data["user"]) if _data.get("user") else None
        self.sort_value: Optional[int] = _data.get("sort_value")
        
        