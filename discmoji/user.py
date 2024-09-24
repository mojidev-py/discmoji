from typing import *

class User:
    def __init__(self,_data: dict):
        self.id: int = int(_data["id"])
        self.username: str = _data["username"]
        self.discriminator: str = _data["discriminator"]
        self.display_name: str = _data["global_name"]
        self.avatar: str = _data["avatar_hash"]
        self.is_bot: bool  = _data["bot"]
        self.is_system: bool = _data["system"]
        self.mfa_enabled: bool = _data["mfa_enabled"]
        self.banner: str = _data["banner"]
        accent_color: int = _data["accent_color"]
        self.accent_color = accent_color.to_bytes().hex()
        self.locale: str = _data["locale"]
        self.flags: int = _data["flags"]
        self.premium_type: int = _data["premium_type"]
        self.public_flags: int = _data["public_flags"]
        self.avatar_dec = _data["avatar_decoration_data"]