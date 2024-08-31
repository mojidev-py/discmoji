from typing import *
import functools


class Command:
    """Represents a prefix command. Not for slash commands, those have a seperate class."""
    def __init__(self,name: str,args: tuple,callback: Coroutine):
        # callback needs to be coroutine because of aiohttp
        self._args = args
        self.callback = callback
        
    
    def error_handler(name: str):
        @functools.wraps()
        def real_deco():
            ...
            return ...
        return real_deco