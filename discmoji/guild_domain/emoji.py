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
from typing import Optional


class Emoji:
    """Represents a discord emoji.
    ## Attributes
    - id - `Optional[discmoji.Snowflake]`
       - The emoji's id.
    - name - `Optional[str]`
       - The emoji's name (may be none in cases of message reactions)
    - roles - `Optional[list[discmoji.Snowflake]]`
       - A list of role ids that are allowed to use this emoji.
    - user - `Optional[User]`
       - The user that created this emoji. May not exist.
    - require_colons - `Optional[bool]`
       - Whether this emoji should be wrapped in colons or not.
    - managed - `Optional[bool]`
       - Whether this emoji is managed
    - animated - `Optional[bool]`
       - Whether this emoji is animated
    - available - `Optional[bool]`
       - Whether this emoji is available. May return false because of server boost benefits.
    """
    def __init__(self, _data: dict):
        self.id: Optional[Snowflake] = Snowflake(_data["id"]) if _data.get("id") is not None else None
        self.name: Optional[str] = _data.get("name")
        self.roles: Optional[list[Snowflake]] = [Snowflake(id) for id in _data.get("roles")]
        self.user: Optional[User] = User(_data["user"]) if _data.get("user") is not None else None
        self.require_colons: Optional[bool] = _data.get("require_colons")
        self.managed: Optional[bool] = _data.get("managed")
        self.animated: Optional[bool] = _data.get("animated")
        self.available: Optional[bool] = _data.get("available")
    