from typing import *
import functools
import asyncio
from asyncio import gather


class Command:
    """Represents a prefix command. Not for slash commands, those have a seperate class."""
    def __init__(self,/,name: str):
        # callback needs to be coroutine because of aiohttp
        self.__error_handlers: List[Callable] = []
        
    # huge credit to AlmostDemoPy! TYSMMM
    
    async def __call__(self, function : Callable | None = None) -> None:
        if not function:
            try:
                return await self.callback()
            except Exception as e:
                tasks = []
                for handler in self.__error_handlers:
                    tasks.append(handler(e))
                await gather(*tasks)
        self.callback : Callable = function
        if not self.name: self.name : str = function.__name__
        self.bot._all_cmds += self
        return self # allows the function ( command object ) to still be used later on in the code

    def error(self, function: Callable) -> None:
        self.__error_handlers.append(function)
