from typing import *
import aiohttp
from .overwrites import ChannelPermissionOverwrite



class GuildTextChannel:
    def __init__(self,_data: dict):
        self.id = int(_data["id"])
        self.type = 0       
        self.position = _data["position"]
        # will be an object once Intents are made
        # goes through each entry in the _data's perm overwrites and makes a class for each overwrite
        self.overwrites = [ChannelPermissionOverwrite(permissionoverwrite) for permissionoverwrite in _data["permission_overwrites"]]
         