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
from .message_domain.message import Message
from .message_domain.embed import Embed
from .message_domain.attachment import Attachment
from ._http import HttpManager
from .exceptions import UnknownHTTPError

class PrefixContext:
    """A class that provides extra data during a `BotCommand`'s invocation."""
    def __init__(self,msg: Message,http: HttpManager):
        self.msg = msg
        self.author = msg.author
        self.__http = http
    
    
    async def send(self,content: str = None,embed: Embed = None,attachments: Attachment = None, **kwargs) -> Message:
        if all((content == None,embed == None,attachments == None,kwargs == None)):
            raise RuntimeError("At least one argument has to be not None.")
        data = {
            "content": content,
            "embeds": [embed]
            # no attachments yet, needs extra logic in request method 
        }
        if embed is None:
            data.pop("embeds")
        rq = await self.__http.request("post",f"channels/{self.msg.channel_id}/messages",data = data,auth=True)
        if rq.status >= 400:
            raise UnknownHTTPError(rq.status,f"Could not send message in channel {self.msg.channel_id}")
        return Message(rq.data)