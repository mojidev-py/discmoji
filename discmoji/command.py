from typing import *
import functools
import asyncio
from asyncio import gather
from .errors import DiscmojiCommandError

class Command:
    """Represents a prefix command. Not for slash commands, those have a separate class."""
    def __init__(self, name: str):
        self.name = name
        self.callback: Optional[Callable] = None
        self.__error_handlers: List[Callable] = []

    def __call__(self, function: Callable) -> 'Command':
        self.callback = function
        return self

    async def invoke(self, *args, **kwargs):
        if self.callback is None:
            raise DiscmojiCommandError(f"Command '{self.name}' has no callback function.")
        try:
            await self.callback(*args, **kwargs)
        except Exception as e:
            tasks = [handler(e) for handler in self.__error_handlers]
            await gather(*tasks)

    def error(self, function: Callable) -> Callable:
        self.__error_handlers.append(function)
        return function

def command(name: str) -> Callable:
    """A decorator that registers a command with the specified name."""
    def decorator(func: Callable) -> Command:
        cmd = Command(name)
        cmd.callback = func
        return cmd
    return decorator
