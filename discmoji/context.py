from typing import *
from .types import EndpointManager,GatewayManager
import asyncio
from .bot import Bot





class Invoked:
    # A class that hosts the data of where a command was used
    def __init__(self,endpoint: EndpointManager,gateway: GatewayManager,bot: Bot):
        self._endpoint = endpoint
        self._gateway  = gateway
        self._bot = bot
        # rest will be constructed by internal funcs
        self.member   = ...
        self.message  = ...
        self.messagerefs = ...
        self.channel  = ...
        self.guild = ...
    
    
    def _is_cmd_invoked(self):
        ... 