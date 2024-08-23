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

import aiohttp
from typing import *
import asyncio
import json
import logging
from colorama import Fore
from random import uniform
import websockets
import os

if TYPE_CHECKING:
  from .member import Member

# very unefficient code, might refine later
# this code doesn't register any commands... yet
class Bot:
    """Represents the discord bot.
    
    ## Attributes:
    - prefix: `str`
      - The prefix to use with the bot.
    - logger: `Logger`
      - Internal attribute.
    - config: `Formatter`
      - Internal Attribute
    - cmds: `Dict[str,function]`
      - stores the command name so when a certain command is located in a message, it activates the callback (the value)
    - token: `str`
      - stores the token
    - ws: `connect`
      - Internal
    """
    # attributes passed to Original class
    #---------------#
    channelid = None
    author = None
    #--------------#
    def __init__(self,prefix: str,sharding: bool,token: str):
        # future me, make sure to add Intents later
        self.prefix = prefix
        self.logger = logging.getLogger(name="inkling")
        self.config = logging.Formatter(Fore.MAGENTA+"[",Fore.RESET+"%(levelname)s-%(asctime)s",Fore.MAGENTA+"]"+Fore.RESET+": %(message)s")
        self.cmds = {}
        self.token = token
        self.ws = websockets.connect("wss://gateway.discord.gg/?v=10&encoding=json")
        # attribute initialized with only one object in it, which is the channel id, and is overrided every single time, for the Original class 
        
        
        super().__init__()
        
    def command(self,name: str,description: str):
      def real_decorator(function):
        def wrapper(*args):
            result = function(*args)
            return result

        return wrapper
      return real_decorator
      # base template code for now, need to focus on actually connecting to the Gateway API
    
    def _get_token(self):
      return self.token
    
      
    async def connect(self,intents: int):
      """Connects your bot with the discord Gateway.

      Args:
          intents (int): A number representing the intents you want the bot to enable. Check the discord dev portal to do the bit math.
      """
      # the intents arg might change later, once I add an Intents class
      async with self.ws as ws:
        loaded = json.loads(await ws.recv())
        HB_INT = loaded["d"]["heartbeat_interval"]
        self.logger.info(f"Establishing heartbeat interval at {HB_INT / 1000} s.")
        # very generalized for now, will elaborate on this later
        await asyncio.sleep(delay=HB_INT + uniform(0,1.00))
        HB_1 = {
          "op": 1,
          "d": ""
        }
        serlzed = json.dumps(HB_1)
        await ws.send(serlzed)
        loaded = json.loads(await ws.recv())
        if loaded["op"] == 11:
          OS = "windows" if os.name == "nt" else "linux"
          IDENTIFY = {
          "op": 2,
          "d": {
            "token": self.token,
            "properties": {
              "os": OS,
              "browser": "discmoji",
              "device": "discmoji"
            },
            "intents":intents
          }
        }
          serlzed = json.dumps(IDENTIFY)
          await ws.send(serlzed)
          recved = json.loads(await ws.recv())
          if recved["v"] is int:
            self.logger.info(f"Logged in as {recved["user"]["username"]}{recved["user"]["discriminator"]}, on gateway session id {recved["session_id"]}.")
          if recved["op"] is int:
            self.logger.fatal(f"Failed to connect to discord gateway with opcode 9. payload: {recved}")
          
          # while True loop handles the heartbeats
          # very basic way of doing this, I might handle this a diff way
          while True:
            asyncio.sleep(delay=HB_INT)
            recved = json.loads(await ws.recv())
            if recved["op"] == 0:
              hb = {
                "op": 1,
                "d": recved["s"]
              }
              serlzed = json.dumps(hb)
              await ws.send(serlzed)
            else:
              hb = {
                "op": 1,
                "d": ""
              }
              serlzed = json.dumps(hb)
              await ws.send(serlzed)
              # the code below this will handle what to do with every event it recieves
              if recved["t"] == "MESSAGE_CREATE":
                self.channelid: int = recved["d"]["channel_id"]
                # member object is initialized here for original to take in
                self.author: Member = Member(id=recved["d"]["author"]["id"],
                                             username=recved["d"]["author"]["username"],
                                             discriminator=recved["d"]["author"]["discriminator"],
                                             global_name=recved["d"]["author"]["global_name"],
                                             avatar=recved["d"]["author"]["avatar"],
                                             mfa_enabled=recved["d"]["author"]["mfa_enabled?"],
                                             banner=recved["d"]["author"]["banner?"],
                                             accent_color=recved["d"]["author"]["accent_color?"],
                                             locale=recved["d"]["author"]["locale?"],
                                             premium_type=recved["d"]["author"]["premium_type?"],
                                             avatar_decoration_data=recved["d"]["author"]["avatar_decoration_data?"]
                                             )
              

                    
            
            
            