from typing import *
import aiohttp



class GuildTextChannel:
    def __init__(self,_data: dict):
        self.id = _data["id"]
        self.type = 0       
        self.position = _data["position"]
        # will be an object once Intents are made
        self.overwrites = _data["permission_overwrites"] 