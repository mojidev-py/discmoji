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
from typing import *
class Message:
    """Represents a message."""
    def __init__(self,
            id: int,
            channel: int,
            author: None,
            timestamp: int,
            mentions: List[None],
            reactions: List[None],
            content: str | None):
        # author is none as a placeholder,
        # so is mentions, because I haven't made a Member object yet
        # reactions is also None, since I have made no Reaction object yet
        # code below this is to allow the initialization vars to become attributes of the original class
        self.id = id
        self.channel = channel
        self.author = author
        self.timestamp = timestamp
        self.mentions = mentions
        self.reactions = reactions
        self.content = content
        
        ...
        # methods will be implemented after I get messages sending