from typing import *
import asyncio
from .channel import GuildTextChannel
from .bot import Bot
from .types import File
import aiohttp
class MessageReference:
    def __init__(self,_data: dict,binded_channel: GuildTextChannel,bindedbot: Bot,id: int):
        self.type = _data["type"]
        self.channel = self.originated_message.channel
        self.guild = self.channel.guild

class Attachment:
    def __init__(self,_data: dict,file: File):
        self.id: int = int(_data["id"])
        self.filename: str  = _data["filename"]
        self.title: str = _data["title"]
        self.description: str = _data["description"]
        self.content_type: str = _data["content_type"]
        self.size: int = _data["size"]
        self.url: str = _data["url"]
        self.proxy_url: str = _data["proxy_url"]
        self.height: int = _data["height"]
        self.width: int = _data["width"]
        self.ephemeral: bool = _data["ephemeral"]
        self.duration_secs: float = _data["duration_secs"]
        self.waveform: bytearray = _data["waveform"]
        self.flags: int = _data["flags"]
        self.__formdata: aiohttp.MultipartWriter = aiohttp.MultipartWriter(boundary="--")
        self.file = file
    def find_content_type(self):
        # only image types gif and png are supported (will add more support)
        name = self.file.filename
        if name.endswith(".gif"):
            return "image/gif"
        if name.endswith(".png"):
            return "image/png"
    
        
    
    
    
    
    def _convert(self):
        with self.__formdata as multipart:
            multipart.append(self.file.filename,{"CONTENT_TYPE":self.find_content_type()})
            multipart.set_content_disposition("form-data",name=f"files[{self.file.__fileindex}]",filename={self.filename})
        # converts data into multipart, haven't implemented turning multiple into attachments, might do that seperately

            

class Embed:
    def __init__(self,_data: dict):
        self.title: str = _data["title"]
        self.type: str = _data["type"]
        self.description: str = _data["description"]
        self.url: str = _data["url"]
        self.timestamp: int = _data["timestamp"]
        self.color: int = _data["color"]
    
    def _dictize(self) -> Dict[str,str | int]:
        # turns self into a dict for msg func to send
        return {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color
        }
    
    # rest are going to be implemented as their own funcs

class Reaction:
    def __init__(self,_data: dict):
        self.count: int = _data["count"]
        self.count_details: dict = {
            "bursts": _data["count_details"]["burst"],
            "normal": _data["count_details"]["normal"]
        }
        self.did_self_react: bool = _data["me"]
        self.did_self_react_burst: bool = _data["me_burst"]
        # emoji is none because no obj for it yet
        self.emoji: ... = ...
        self.burst_colors: list[int] = _data["burst_colors"]
        