from typing import *
from .user import User
from .bot import Bot
import asyncio

class Emoji:
    def __init__(self,dict: dict,bot: Bot):
        self.id: Optional[int] = str(dict.get("id")) if dict.get("id") is not None else None
        self.name: Optional[str] = dict.get("name")
        self.roles: Optional[list[int]] = dict.get("roles")
        self.user: Optional[User] = User(asyncio.run(bot._http.send_request('get',f"/users/{dict.get("user")}")).data) if dict.get("user") is not None else None
        self.require_colon: Optional[bool] = dict.get("require_colon")
        self.managed: Optional[bool] = dict.get("managed")
        self.animated: Optional[bool] = dict.get("animated")
        self.available: Optional[bool] = dict.get("available")