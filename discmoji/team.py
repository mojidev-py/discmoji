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