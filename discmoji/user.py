from typing import *

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