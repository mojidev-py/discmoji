from typing import *
from .types import EndpointManager,GatewayManager
import asyncio
from .bot import Bot





class Invoked:
    # A class that hosts the data of where a command was used
    def __init__(self,endpoint: EndpointManager,gateway: GatewayManager,bot: Bot):
        self._endpoint = endpoint
        self._gateway = gateway
        self._bot = bot
        # rest will be constructed by internal funcs
        self.member = ...
        self.message = ...
        self.messagerefs = ...
        self.channel = ...
        self.guild = ...
    
    
    def _is_cmd_invoked(self) -> bool:
        recieved = self._gateway.current_payload
        if recieved.event_name == "MESSAGE_CREATE":    
            for cmd in self._bot._all_cmds:
                if cmd in recieved.data["content"]:
                    asyncio.run(cmd.callback)
                    return (True,cmd)
        return False 
    
    
    def _construct(self):
        if self._is_cmd_invoked:
            ...
            # need to make classes for member, message, and that stuff