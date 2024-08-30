"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from typing import *
import aiohttp
from .types import (GatewayManager,EndpointManager)


class Bot:
    """Represents the application."""
    def __init__(self,token: str,intents: int):
        self._http = EndpointManager(token=token)
        self._gateway_client = GatewayManager(token=token,intents=intents,endpointclient=self._http)
        self.token = token
        self.intents = intents
        self._all_cmds = []
    
    async def connect(self):
        # this just inits the gateway connection
        await self._gateway_client._hand_shake()
        # self-explanatory, handles the heartbeats
        await self._gateway_client._handle_heartbeats()
    
    def command(name: str):
        """A decorator that registers a command with the specified name."""
        def decorator(*args, **kwargs):
            ...
            return ...
            # placeholder code before I start to make the command object
        return decorator
    
             
    
    
        
    

                    
            
            
            