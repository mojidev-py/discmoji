from typing import *
from .message import Message
import asyncio
from .channel import GuildTextChannel
from .bot import Bot

class MessageReference:
    def __init__(self,_data: dict,binded_channel: GuildTextChannel,bindedbot: Bot,id: int):
        self.type = _data["type"]
        self.originated_message = Message(asyncio.run(bindedbot._http.send_request('get',f'/channels/{binded_channel.id}/messages/{_data["message_reference"]["message_id"]}')).data)
        self.channel = self.originated_message.channel
        self.guild = self.channel.guild
        self.resolved = Message(asyncio.run(bindedbot._http.send_request('get',f'/channels/{binded_channel.id}/{id}')))

class Attachment:
    def __init__(self,_data: dict):
        self.id: int = int(_data["id"])
        self.filename: str = _data["filename"]
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

class Embed:
    def __init__(self,_data: dict):
        self.title: str = _data["title"]
        self.type: str = _data["type"]
        self.description: str = _data["description"]
        self.url: str = _data["url"]
        self.timestamp: int = _data["timestamp"]
        self.color: int = _data["color"]
    
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
        