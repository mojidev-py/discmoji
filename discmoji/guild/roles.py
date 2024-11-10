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
class Role:
    """Represents a discord Role.
    ## Attributes
    - id - `discmoji.Snowflake`
       - ID of the role
    - name - `str`
       - Name of the role
    - color - `str`
       - Hex code for color of the role.
    - hoist - `bool`
       - Whether this role is pinned in the server role listing.
    - icon - `Optional[str]`
       - Formatted cdn link leading to icon of role, if it exists."""
    def __init__(self,_data: dict[str,str | int | dict | bool]):
        self.id = Snowflake(_data["id"])
        self.name: str = _data["name"]
        self.color = _data["color"].to_bytes().hex()
        self.hoist: bool = _data["hoist"]
        self.icon: Optional[str] = f"https://cdn.discordapp.com/role_icons/{int(self.id)}/{_data.get("icon")}.png" if _data.get("icon") is not None else None