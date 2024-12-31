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


class Listener:
    """Represents a listener for a certain gateway event. Fires callback once it recieves one.
    Also allows you to implement checks to further filter through events.
    ## Note
    The check feature requires you to implement the check for a RAW payload. As of v0.1.2, no abstraction for an event has been implemented yet. Will be implemented next update.
    
    Event names are listed in the discord developer documentation.
    Event names should be entered like this: 'message_create', as the listener will do the name matching for you."""
    def __init__(self,name: str,check: Callable = None):
        self.name = name
        self.check = check
    
    
    def __call__(self,func: Callable):
        self.callback = func
        self.bot._listeners.append(self)
                    
            
            
            
        