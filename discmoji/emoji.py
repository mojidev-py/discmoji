from typing import *
from .roles import Role
from .user import User
from ._http import EndpointManager
import asyncio

class Emoji:
    def __init__(self,dict: dict,endpoint: EndpointManager):
        self.id: int = self._get_dict_value(dict, "id")
        self.name: str = self._get_dict_value(dict, "name")
        self.roles: list[int] = self._get_dict_value(dict, "roles", [])
        self.user: User = User(asyncio.run(endpoint.send_request('get',f"/users/{self._get_dict_value(dict, 'user')}")).data)
        self.require_colon: bool = self._get_dict_value(dict, "require_colon", False)
        self.managed: bool = self._get_dict_value(dict, "managed", False)
        self.animated: bool = self._get_dict_value(dict, "animated", False)
        self.available: bool = self._get_dict_value(dict, "available", False)

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
