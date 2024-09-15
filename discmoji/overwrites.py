from typing import *
from .bot import Bot
from .guild import Guild
import asyncio

class ChannelPermissionOverwrite:
    
    def __init__(self,_data: dict,__bindedbot: Bot,__bindedguild: Guild):
        try:
            self.role = asyncio.run(__bindedbot._http.send_request('get',f'/guilds/{__bindedguild.id}/roles/{_data["permission_overwrites"]["id"] if _data["permission_overwrites"] else None}'))
        except Exception:
            # placeholder, since no role obj yet
            self.roles = [... for asyncio.run(__bindedbot._http.send_request('get',f'/guilds/{__bindedguild.id}/roles/{_data["permission_overwrites"]["id"]}')) in _data["permission_overwrites"]]
        self.allowed_perms = 0
        self.disabled_perms = 0 
        