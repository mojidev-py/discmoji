from typing import *
from ._http import EndpointManager

class User:
    def __init__(self,_data: dict):
        self.id: Optional[int] = int(_data.get("id"))
        self.username: Optional[str] = _data.get("username")
        self.discriminator: Optional[str] = _data.get("discriminator")
        self.display_name: Optional[str] = _data.get("global_name")
        self.avatar: Optional[str] = _data.get("avatar_hash")
        self.is_bot: Optional[bool]  = _data.get("bot")
        self.is_system: Optional[bool] = _data.get("system")
        self.mfa_enabled: Optional[bool] = _data.get("mfa_enabled")
        self.banner: Optional[str] = _data.get("banner")
        accent_color: Optional[int] = _data.get("accent_color")
        self.accent_color = accent_color.to_bytes().hex()
        self.locale: Optional[str] = _data.get("locale")
        self.flags: Optional[int] = _data.get("flags")
        self.premium_type: Optional[int] = _data.get("premium_type")
        self.public_flags: Optional[int] = _data.get("public_flags")
        self.avatar_dec: Optional[str] = _data.get("avatar_decoration_data")

    async def edit_user(self, user_id: int, username: Optional[str] = None, avatar: Optional[str] = None, banner: Optional[str] = None, accent_color: Optional[int] = None):
        data = {
            "username": username,
            "avatar": avatar,
            "banner": banner,
            "accent_color": accent_color
        }
        await self._http.send_request('patch', f'/users/{user_id}', data=data)

    async def get_user(self, user_id: int) -> 'User':
        response = await self._http.send_request('get', f'/users/{user_id}')
        return User(response.data)

    async def delete_user(self, user_id: int):
        await self._http.send_request('delete', f'/users/{user_id}')
