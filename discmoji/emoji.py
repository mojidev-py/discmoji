from typing import *
from .roles import Role
from .user import User
from ._http import EndpointManager
import asyncio

class Emoji:
    def __init__(self,dict: dict,endpoint: EndpointManager):
        self.id: int = str(dict["id"])
        self.name: str = dict["name"]
        self.roles: list[int] = dict["roles"]
        self.user: User = User(asyncio.run(endpoint.send_request('get',f"/users/{dict["user"]}")).data)
        self.require_colon: bool = dict["require_colon"]
        self.managed: bool = dict["managed"]
        self.animated: bool = dict["animated"]
        self.available: bool = dict["available"]