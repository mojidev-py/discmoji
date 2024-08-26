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
    # attributes passed to Original class (might make a gateway obj for connect())
    #---------------#
    channelid = None
    author = None
    #--------------#
    def __init__(self,prefix: str,sharding: bool,token: str):
        # future me, make sure to add Intents later
        self.prefix = prefix
        self.logger = logging.getLogger(name="inkling")
        self.config = logging.Formatter(Fore.MAGENTA+"[",Fore.RESET+"%(levelname)s-%(asctime)s",Fore.MAGENTA+"]"+Fore.RESET+": %(message)s")
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

              

                    
            
            
            