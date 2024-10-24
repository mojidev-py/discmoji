from typing import *
import asyncio
from .channel import GuildTextChannel
from .bot import Bot
from .types import File
import aiohttp
from .emoji import Emoji
class MessageReference:
    def __init__(self,_data: dict,binded_channel: GuildTextChannel,bindedbot: Bot,id: Optional[int]):
        self.type = _data["type"]
        self.channel = self.originated_message.channel
        self.guild = self.channel.guild

class Attachment:
    def __init__(self,_data: dict,file: File):
        self.id: Optional[int] = int(_data["id"])
        self.filename: Optional[str]  = _data.get("filename")
        self.title: Optional[str] = _data.get("title")
        self.description: Optional[str] = _data.get("description")
        self.content_type: Optional[str] = _data.get("content_type")
        self.size: Optional[int] = _data.get("size")
        self.url: Optional[str] = _data.get("url")
        self.proxy_url: Optional[str] = _data.get("proxy_url")
        self.height: Optional[int] = _data.get("height")
        self.width: Optional[int] = _data.get("width")
        self.ephemeral: Optional[bool] = _data.get("ephemeral")
        self.duration_secs: Optional[float] = _data.get("duration_secs")
        self.waveform: Optional[bytearray] = _data.get("waveform")
        self.flags: Optional[int] = _data["flags"]
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
        self.title: Optional[str] = _data.get("title")
        self.type: Optional[str] = _data.get("type")
        self.description: Optional[str] = _data.get("description")
        self.url: Optional[str] = _data.get("url")
        self.timestamp: Optional[int] = _data.get("timestamp")
        self.color: Optional[int] = _data.get("color")
    
    def _dictize(self) -> Dict[Optional[str],Optional[str] | Optional[int]]:
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
    def __init__(self,_data: dict,bot: Bot):
        self.count: Optional[int] = _data.get("count")
        self.count_details: dict = {
            "bursts": _data.get("count_details")["burst"],
            "normal": _data.get("count_details")["normal"]
        }
        self.did_self_react: Optional[bool] = _data.get("me")
        self.did_self_react_burst: Optional[bool] = _data.get("me_burst")
        self.emoji: Emoji = Emoji(_data.get("emoji"),bot)
        self.burst_colors: list[Optional[int]] = int(_data.get("afk_channel_id"))
        