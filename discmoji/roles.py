from typing import *
from .types import RoleTags



class Role:
    def __init__(self, _data: dict | None):
        self.id: int = _data["id"]
        self.name: str = _data["name"]
        self.color: int = hex(_data["color"])
        self.hoist: bool = _data["hoist"]
        self.icon: str = _data["icon"]
        self.emoji: str = _data["unicode_emoji"]
        self.position: int = _data["position"]
        # permissions is int for now, going to change in overwrites.py
        self.permissions: int =  int(_data["permissions"])
        self.managed_by_integration: bool = _data["managed"]
        self.mentionable: bool = _data["mentionable"]
        self.tags: RoleTags = RoleTags(_data["tags"])
        self.flags: int = _data["flags"]
        