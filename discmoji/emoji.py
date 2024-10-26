from typing import *
from .roles import Role
from .user import User
from .bot import Bot
import asyncio

class Emoji:
    def __init__(self,dict: dict,bot: Bot):
        self.id: Optional[int] = str(dict.get("id")) if dict.get("id") is not None else None
        self.name: Optional[str] = dict.get("name")
        self.roles: Optional[list[int]] = dict.get("roles")
        self.user: Optional[User] = User(asyncio.run(bot._http.send_request('get',f"/users/{dict.get("user")}")).data) if dict.get("user") is not None else None
        self.require_colon: Optional[bool] = dict.get("require_colon")
        self.managed: Optional[bool] = dict.get("managed")
        self.animated: Optional[bool] = dict.get("animated")
        self.available: Optional[bool] = dict.get("available")

    async def create_emoji(self, guild_id: int, name: str, image: str, roles: Optional[List[int]] = None) -> 'Emoji':
        data = {
            "name": name,
            "image": image,
            "roles": roles
        }
        response = await self.bot._http.send_request('post', f'/guilds/{guild_id}/emojis', data=data)
        return Emoji(response.data, self.bot)

    async def delete_emoji(self, guild_id: int, emoji_id: int):
        await self.bot._http.send_request('delete', f'/guilds/{guild_id}/emojis/{emoji_id}')

    async def edit_emoji(self, guild_id: int, emoji_id: int, name: Optional[str] = None, roles: Optional[List[int]] = None):
        data = {
            "name": name,
            "roles": roles
        }
        await self.bot._http.send_request('patch', f'/guilds/{guild_id}/emojis/{emoji_id}', data=data)
