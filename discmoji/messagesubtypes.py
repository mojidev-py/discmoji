from typing import *
import asyncio
from .channel import GuildTextChannel
from .bot import Bot
from .types import File
import aiohttp

class MessageReference:
    def __init__(self, _data: dict, binded_channel: GuildTextChannel, bindedbot: Bot, id: int):
        self.type = self._get_dict_value(_data, "type")
        self.channel = self._get_dict_value(self.originated_message, "channel")
        self.guild = self._get_dict_value(self.channel, "guild")

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)

class Attachment:
    def __init__(self, _data: dict, file: File):
        self.id: int = self._get_dict_value(_data, "id")
        self.filename: str = self._get_dict_value(_data, "filename")
        self.title: str = self._get_dict_value(_data, "title")
        self.description: str = self._get_dict_value(_data, "description")
        self.content_type: str = self._get_dict_value(_data, "content_type")
        self.size: int = self._get_dict_value(_data, "size")
        self.url: str = self._get_dict_value(_data, "url")
        self.proxy_url: str = self._get_dict_value(_data, "proxy_url")
        self.height: int = self._get_dict_value(_data, "height")
        self.width: int = self._get_dict_value(_data, "width")
        self.ephemeral: bool = self._get_dict_value(_data, "ephemeral")
        self.duration_secs: float = self._get_dict_value(_data, "duration_secs")
        self.waveform: bytearray = self._get_dict_value(_data, "waveform")
        self.flags: int = self._get_dict_value(_data, "flags")
        self.__formdata: aiohttp.MultipartWriter = aiohttp.MultipartWriter(boundary="--")
        self.file = file

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)

    def find_content_type(self):
        # only image types gif and png are supported (will add more support)
        name = self.file.filename
        if name.endswith(".gif"):
            return "image/gif"
        if name.endswith(".png"):
            return "image/png"

    def _convert(self):
        with self.__formdata as multipart:
            multipart.append(self.file.filename, {"CONTENT_TYPE": self.find_content_type()})
            multipart.set_content_disposition("form-data", name=f"files[{self.file.__fileindex}]", filename={self.filename})
        # converts data into multipart, haven't implemented turning multiple into attachments, might do that separately

class Embed:
    def __init__(self, _data: dict):
        self.title: str = self._get_dict_value(_data, "title")
        self.type: str = self._get_dict_value(_data, "type")
        self.description: str = self._get_dict_value(_data, "description")
        self.url: str = self._get_dict_value(_data, "url")
        self.timestamp: int = self._get_dict_value(_data, "timestamp")
        self.color: int = self._get_dict_value(_data, "color")

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)

    def _dictize(self) -> Dict[str, str | int]:
        # turns self into a dict for msg func to send
        return {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color
        }

class Reaction:
    def __init__(self, _data: dict):
        self.count: int = self._get_dict_value(_data, "count")
        self.count_details: dict = {
            "bursts": self._get_dict_value(_data["count_details"], "burst"),
            "normal": self._get_dict_value(_data["count_details"], "normal")
        }
        self.did_self_react: bool = self._get_dict_value(_data, "me")
        self.did_self_react_burst: bool = self._get_dict_value(_data, "me_burst")
        # emoji is none because no obj for it yet
        self.emoji: ... = ...
        self.burst_colors: list[int] = self._get_dict_value(_data, "burst_colors")

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
