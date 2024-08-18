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
if TYPE_CHECKING:
  from ._member import InternalMember

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
    
    
    
    
    
    
    async def connect():
      """Connects the bot to discord."""
      
      
                    
                    
            
            
            