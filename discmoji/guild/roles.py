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
from .._http import HttpManager

class Role:
    """Represents a discord Role.
    ## Attributes
    - id - `discmoji.Snowflake`
       - Contains the id of the role.
    - name - `str`
       - Contains the name of the role.
    - color - `int`
       - Contains the color of the role.
    - hoist - `bool`
       - Indicates whether the role is hoisted (displayed separately) in the member list.
    - position - `int`
       - Contains the position of the role in the guild's role hierarchy.
    - permissions - `str`
       - Contains the permissions of the role.
    - managed - `bool`
       - Indicates whether the role is managed by an integration.
    - mentionable - `bool`
       - Indicates whether the role is mentionable.
    """
    def __init__(self,_data: dict[str,str | int | dict]):
        self.id = Snowflake(_data["id"])
        self.name: str = _data["name"]
        self.color: int = _data["color"]
        self.hoist: bool = _data["hoist"]
        self.position: int = _data["position"]
        self.permissions: str = _data["permissions"]
        self.managed: bool = _data["managed"]
        self.mentionable: bool = _data["mentionable"]

    async def create_role(self, http: HttpManager, guild_id: Snowflake, name: str, color: Optional[int] = None, hoist: Optional[bool] = None, position: Optional[int] = None, permissions: Optional[str] = None, mentionable: Optional[bool] = None):
        """Creates a new role in the guild."""
        data = {"name": name}
        if color is not None:
            data["color"] = color
        if hoist is not None:
            data["hoist"] = hoist
        if position is not None:
            data["position"] = position
        if permissions is not None:
            data["permissions"] = permissions
        if mentionable is not None:
            data["mentionable"] = mentionable
        response = await http.request("post", f"guilds/{guild_id}/roles", auth=True, data=data)
        return Role(response.data)

    async def delete_role(self, http: HttpManager, guild_id: Snowflake, role_id: Snowflake):
        """Deletes a role from the guild."""
        await http.request("delete", f"guilds/{guild_id}/roles/{role_id}", auth=True)
