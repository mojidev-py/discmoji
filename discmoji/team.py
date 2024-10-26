from typing import Optional, List
from .types import TeamMember
from ._http import EndpointManager
from .user import User
import asyncio


class Team:
    def __init__(self,_dict: dict,http:EndpointManager):
        self.icon: Optional[str] = _dict.get("icon")
        self.id: int = int(_dict.get("id"))
        self.members: List[TeamMember] = [TeamMember(member) for member in _dict.get("members")]
        self.name: str = _dict.get("name")
        self.owner: User = User(asyncio.run(http.send_request("get",f"/users/{_dict.get("team_owner_id")}")).data) 

    async def create_team(self, name: str, owner_id: int) -> 'Team':
        data = {
            "name": name,
            "owner_id": owner_id
        }
        response = await self.http.send_request('post', '/teams', data=data)
        return Team(response.data, self.http)

    async def delete_team(self, team_id: int):
        await self.http.send_request('delete', f'/teams/{team_id}')

    async def edit_team(self, team_id: int, name: Optional[str] = None, icon: Optional[str] = None):
        data = {
            "name": name,
            "icon": icon
        }
        await self.http.send_request('patch', f'/teams/{team_id}', data=data)

    async def add_member(self, team_id: int, user_id: int):
        await self.http.send_request('put', f'/teams/{team_id}/members/{user_id}')

    async def remove_member(self, team_id: int, user_id: int):
        await self.http.send_request('delete', f'/teams/{team_id}/members/{user_id}')
