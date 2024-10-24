from typing import *
from .channel import GuildTextChannel
from .bot import Bot
import asyncio
from .user import User
from .guild import Guild
from .roles import Role
from .messagesubtypes import MessageReference, Attachment, Embed, Reaction


class Message:
    def __init__(self,_data: dict, bot: Bot,binded_guild: Guild):
        self.id: int = _data["id"]
        self.channel: GuildTextChannel = GuildTextChannel(asyncio.run(bot._http.send_request('get',f'/channels/{self._get_dict_value(_data, "channel_id")}')).data)
        self.author: User = User(self._get_dict_value(_data, "author"))
        self.content: str = self._get_dict_value(_data, "content")
        self.timestamp: int = self._get_dict_value(_data, "timestamp")
        self.edited_timestamp: int = self._get_dict_value(_data, "edited_timestamp")
        self.tts: bool = self._get_dict_value(_data, "tts", False)
        self.mentioned_everyone: bool = self._get_dict_value(_data, "mention_everyone", False)
        self.mentions = [User(user) for user in self._get_dict_value(_data, "mentions", [])]
        self.mentioned_roles: list[Role] = [User(asyncio.run(bot._http.send_request('get',f'/guilds/{binded_guild.id}/roles/{roleid["id"]}')).data) for roleid in self._get_dict_value(_data, "mention_roles", [])]
        self.channel_mentions: list[GuildTextChannel] = [GuildTextChannel(asyncio.run(bot._http.send_request('get',f'/channels/{channelid["id"]}')).data) for channelid in self._get_dict_value(_data, "mention_channels", [])]
        self.attachments = [Attachment(attachment) for attachment in self._get_dict_value(_data, "attachments", [])]
        self.embeds = [Embed(embed) for embed in self._get_dict_value(_data, "embeds", [])]
        self.reactions = [Reaction(reaction) for reaction in self._get_dict_value(_data, "reactions", [])]
        self.pinned: bool = self._get_dict_value(_data, "pinned", False)
        self.webhook_id: int = int(self._get_dict_value(_data, "webhook_id"))
        self.type: int = self._get_dict_value(_data, "type")
        self.reply_data: MessageReference = MessageReference(self._get_dict_value(_data, "message_reference"))

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
