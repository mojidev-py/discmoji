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
from random import uniform


# very unefficient code, might refine later
class Bot:
    """Represents the discord bot.
    
    ## Attributes:
    - prefix: `str`
      - The prefix to use with the bot.
    - logger: `Logger`
      - Internal attribute.
    - config: `Formatter`
      - Internal Attribute
    """
    def __init__(self,prefix: str,sharding: bool):
        # future me, make sure to add Intents later
        self.prefix = prefix
        self.logger = logging.getLogger(name="inkling")
        self.config = logging.Formatter(Fore.MAGENTA+"[",Fore.RESET+"%(levelname)s-%(asctime)s",Fore.MAGENTA+"]"+Fore.RESET+": %(message)s")
        
    
    def command(name: str):
      """A decorator that registers a command."""
      ...
    
    
    
    
    
    
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
            # |
            # V
            # This code is a bit weird since this starts before the heart beat
            if recvd["code"] is int:
                if recvd["code"] == 4000:
                    self.logger.fatal(msg=f"Encountered a unknown error when trying to connect to gateway socket. Payload recieved:{recvd}")
                    await ws.close()
                if recvd["code"] == 4014:
                    self.logger.fatal(msg=f"The bot is running with intents that have not been approved through the Discord Developer Portal. Bot may not work as expected. Payload recieved:{recvd}")
                    await ws.close()
                if recvd["code"] == 4011:
                    self.logger.fatal(msg=f"The gateway API is stopping you from running this. This instance would have covered too much guilds. When using Bot, set the sharding attribute to True. Payload: {recvd}")
                    await ws.close()
                if recvd["code"] == 4009:
                    self.logger.fatal(msg=f"Connection was timed out. Payload: {recvd}")
                    await ws.close()
            # establishing heartbeat and ACKs, not sure if discord gateway provides jitter or not
            await asyncio.sleep(delay=hb_int * uniform(0,1.00))
            await ws.send(message={
              "op": 1,
              "d" : {}
            })
            recvd = json.loads(await ws.recv())
            if recvd["op"] == 11:
              while True: # prob not the best way to do this ;(
                await asyncio.sleep(delay=hb_int)
                await ws.send(message={
                  "op": 1,
                  "d": {
                    # placeholder, I need to make classes for members, api calls and such before doing this
                  }})
              
                    
                    
            
            
            