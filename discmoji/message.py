from typing import *
from .channel import GuildTextChannel
from .bot import Bot
import asyncio
from .user import User
from .guild import Guild
from .roles import Role


class Message:
    def __init__(self,_data: dict, bot: Bot,binded_guild: Guild):
        self.id: int = _data["id"]
        self.channel: GuildTextChannel = GuildTextChannel(asyncio.run(bot._http.send_request('get',f'/channels/{_data["channel_id"]}')).data)
        self.author: User = User(_data["author"])
        self.content: str = _data["content"]
        self.timestamp: int = _data["timestamp"]
        self.edited_timestamp: int = _data["edited_timestamp"]
        self.tts: bool = _data["tts"]
        self.mentioned_everyone: bool = _data["mention_everyone"]
        self.mentions = [User(user) for user in _data["mentions"]]
        self.mentioned_roles: list[Role] = [User(asyncio.run(bot._http.send_request('get',f'/guilds/{binded_guild.id}/roles/{roleid["id"]}')).data) for roleid in _data["mention_roles"]]
        self.channel_mentions: list[GuildTextChannel] = [GuildTextChannel(asyncio.run(bot._http.send_request('get',f'/channels/{channelid["id"]}')).data) for channelid in _data["mention_channels"]]
        # yes, ik that the names ending in "id" are pretty redundant names, but who really cares, i can edit that later
        self.attachments,self.embeds,self.reactions = ...,...,...
        # the ones that are assigned an ellipsis are the ones that need an object for them
        self.pinned: bool = _data["pinned"]
        self.webhook_id: int = int(_data["webhook_id"])
        self.type: int = _data["type"]
        ...
        # rest need tons of new objects i'm too lazy to implement rn