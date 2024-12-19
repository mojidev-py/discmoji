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
SOFTWARE.
"""
from typing import Callable
import warnings
import asyncio

class BotCommand:
    def __init__(self,name: str, /):
        self.name = name
        self.error_handlers = []
    
    def __call__(self,function: Callable):
        if not function:
            try:
                return self.callback()
            except:
                tasks = []
                for handler in self.error_handlers:
                    tasks.append(handler)
                asyncio.run(*tasks)
        self.callback = function
        self.bot._commands.append(self)
        if not self.name: self.name : str = function.__name__
        return self
    
    
    
    def error(self):
        warnings.warn("Prefix commands are highly discouraged for public bot development. We offer this option only for people that NEED prefix commands.",DeprecationWarning)
        """A decorator for handling errors that may occur while running this command's invocation.
        All error handlers you describe for this command have to have a type inheriting from Exception as their first argument."""
        def decorator(func: Callable):
            self.error_handlers.append(func)
        return decorator