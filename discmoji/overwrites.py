from typing import *
from .bot import Bot
from .guild import Guild
import asyncio

class ChannelPermissionOverwrites:
    
    def __init__(self,_data: dict,__bindedbot: Bot,__bindedguild: Guild):
        self.role = asyncio.run(__bindedbot._http.send_request('get',f'/guilds/{__bindedguild.id}/roles/{_data["permission_overwrites"] if len(_data["permission_overwrites"]) > 1 else None}'))
        # else None will be handled in another attribute, (roles)
        self.allowed_perms = 0
        self.disabled_perms = 0 