from typing import *
from .types import RoleTags
from ._http import EndpointManager

class Role:
    def __init__(self, _data: dict | None, __bindedhttp: EndpointManager):
        self.id: int = _data["id"]
        self.name: str = _data["name"]
        self.color: int = hex(_data["color"])
        self.hoist: bool = _data["hoist"]
        self.icon: str = _data["icon"]
        self.emoji: str = _data["unicode_emoji"]
        self.position: int = _data["position"]
        self.permissions: int = int(_data["permissions"])
        self.managed_by_integration: bool = _data["managed"]
        self.mentionable: bool = _data["mentionable"]
        self.tags: RoleTags = RoleTags(_data["tags"])
        self.flags: int = _data["flags"]
        self.__bindedhttp = __bindedhttp

    async def create_role(self, guild_id: int, name: str, color: Optional[int] = None, hoist: Optional[bool] = None, mentionable: Optional[bool] = None, permissions: Optional[int] = None) -> 'Role':
        data = {
            "name": name,
            "color": color,
            "hoist": hoist,
            "mentionable": mentionable,
            "permissions": permissions
        }
        response = await self.__bindedhttp.send_request('post', f'/guilds/{guild_id}/roles', data=data)
        return Role(response.data, self.__bindedhttp)

    async def delete_role(self, guild_id: int, role_id: int):
        await self.__bindedhttp.send_request('delete', f'/guilds/{guild_id}/roles/{role_id}')

    async def edit_role(self, guild_id: int, role_id: int, name: Optional[str] = None, color: Optional[int] = None, hoist: Optional[bool] = None, mentionable: Optional[bool] = None, permissions: Optional[int] = None):
        data = {
            "name": name,
            "color": color,
            "hoist": hoist,
            "mentionable": mentionable,
            "permissions": permissions
        }
        await self.__bindedhttp.send_request('patch', f'/guilds/{guild_id}/roles/{role_id}', data=data)
