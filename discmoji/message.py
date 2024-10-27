from typing import *
from .bot import Bot
import asyncio
from .user import User
from .guild import Guild
from .roles import Role
from .messagesubtypes import MessageReference, Attachment, Embed, Reaction
# removed all dependencies with guildtextchannel since it needs to be able to retrieve a message


class Message:
    def __init__(self,_data: dict, bot: Bot,binded_guild: Guild):
        self.id: Optional[int] = _data["id"]
        self.channel: Optional[int] = _data.get("channel_id")
        self.author: Optional[User] = User(_data.get("author"))
        self.content: Optional[str] = _data.get("content")
        self.timestamp: Optional[int] = _data.get("timestamp")
        self.edited_timestamp: Optional[int] = _data.get("edited_timestamp")
        self.tts: Optional[bool] = _data.get("tts")
        self.mentioned_everyone: Optional[bool] = _data.get("mention_everyone")
        self.mentions = [User(user) for user in _data.get("mentions") if _data.get("mentions") is not None]
        self.mentioned_roles: Optional[list[Role]] = [User(asyncio.run(bot._http.send_request('get',f'/guilds/{binded_guild.id}/roles/{roleid["id"]}')).data) for roleid in _data.get("mention_roles")]
        # channel_mentions is deprecated because of circular imports
        self.attachments = [Attachment(attachment) for attachment in _data.get("attachments") if _data.get("attachments") is not None]
        self.embeds = [Embed(embed) for embed in _data.get("embeds") if _data.get("embeds") is not None]
        self.reactions = [Reaction(reaction) for reaction in _data.get("reactions") if _data.get("reactions") is not None]
        self.pinned: Optional[bool] = _data.get("pinned")
        self.webhook_id: Optional[int] = int(_data.get("webhook_id")) if _data.get("webhook_id") is not None else None
        self.type: Optional[int] = _data.get("type")
        self.reply_data: Optional[MessageReference] = MessageReference(_data.get("message_reference")) if _data.get("message_reference") is None else None

