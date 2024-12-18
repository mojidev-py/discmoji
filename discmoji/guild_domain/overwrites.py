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
from .._types import Permissions
from typing import Literal

class PermissionOverwrite:
    """Represents an overwrite over original permissions.
    ## Attributes
    - id - `discmoji.Snowflake`
      - the ID of the overwrite.
    - type - `Literal["role","member"]`
      - Indicates whether this overwrite applies to a role, or a specific member.
    - allowed - `discmoji.Permissions`
      - Permissions object with all allowed permissions set to True."""
    def __init__(self, _data: dict):
        self.id: Snowflake = Snowflake(_data["id"])
        self.type: Literal["role","member"]= "role" if _data["type"] == 0 else "member"
        self.allowed = Permissions._convert_perms(_data["allow"])
        