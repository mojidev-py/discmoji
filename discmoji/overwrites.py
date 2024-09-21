from typing import *
from .bot import Bot
from .guild import Guild
import asyncio
from .roles import Role

class ChannelPermissionOverwrite:
    
    def __init__(self,_data: dict,__bindedbot: Bot,__bindedguild: Guild):
        self.role = asyncio.run(__bindedbot._http.send_request('get',f'/guilds/{__bindedguild.id}/roles/{_data["permission_overwrites"]["id"] if _data["permission_overwrites"] else None}'))
        self.allowed_perms = 0
        self.disabled_perms = 0 