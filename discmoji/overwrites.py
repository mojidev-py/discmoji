from typing import *
from .bot import Bot
from .guild import Guild
import asyncio

class ChannelPermissionOverwrites:
    
    def __init__(self,_data: dict,__bindedbot: Bot,__bindedguild: Guild):
        try:
            self.role = asyncio.run(__bindedbot._http.send_request('get',f'/guilds/{__bindedguild.id}/roles/{_data["permission_overwrites"]["id"] if len(_data["permission_overwrites"]) > 1 else None}'))
        except Exception as e:
            self.roles = ...
        self.allowed_perms = 0
        self.disabled_perms = 0 
        