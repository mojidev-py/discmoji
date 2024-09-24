from typing import *
from .channel import GuildTextChannel
from .bot import Bot
import asyncio


class Message:
    def __init__(self,_data: dict, bot: Bot):
        self.id: int = _data["id"]
        self.channel: GuildTextChannel = GuildTextChannel(asyncio.run(bot._http.send_request('get',f'/channels/{_data["channel_id"]}')).data)
        