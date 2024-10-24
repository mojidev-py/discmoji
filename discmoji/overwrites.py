from typing import *
from .bot import Bot
from .guild import Guild
import asyncio
from .roles import Role

class ChannelPermissionOverwrite:
    
    def __init__(self,_data: dict,__bindedbot: Bot,__bindedguild: Guild):
        self.roles: Optional[list[Role]] = [Role(asyncio.run(__bindedbot._http.send_request("get",f"guilds/{__bindedguild.id}/{roleid["id"]}"))) for roleid in _data.get("permission_overwrites")]
        # may return a empty object if roles is not a role id
        self.allowed_perms: Optional[int] = int(_data.get("allow")) if _data.get("allow") is not None else None
        self.disabled_perms: Optional[int] = int(_data.get("deny")) if _data.get("deny") is not None else None