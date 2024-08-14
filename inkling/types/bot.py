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

import websockets
from typing import *
import asyncio
import json
import logging
from colorama import Fore



class Bot:
    def __init__(self,prefix: str):
        # future me, make sure to add Intents later
        self.prefix = prefix
        self.logger = logging.getLogger(name="inkling")
        self.config = logging.Formatter(Fore.MAGENTA+"[",Fore.RESET+"%(levelname)s-%(asctime)s",Fore.MAGENTA+"]"+Fore.RESET+": %(message)s")
        
    
    async def connect(self,token: str) -> None:
        """Connects to your Discord bot.
        ## Args
        - `token` - `str`
          - The token that allows the library to authenticate to the API"""
        ws = websockets.connect("wss://gateway.discord.gg/?v=10&encoding=json")
        async with ws as ws:
            recvd = json.loads(await ws.recv())
            hb_int = recvd["d"]["heartbeat_interval"]
            self.logger.info(msg=f"Successfully connected to gateway. Establishing shard heartbeat of {hb_int / 1000}s.")
            
            
            