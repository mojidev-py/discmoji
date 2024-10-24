from typing import *

class User:
    def __init__(self,_data: dict):
        self.id: int = self._get_dict_value(_data, "id")
        self.username: str = self._get_dict_value(_data, "username")
        self.discriminator: str = self._get_dict_value(_data, "discriminator")
        self.display_name: str = self._get_dict_value(_data, "global_name")
        self.avatar: str = self._get_dict_value(_data, "avatar_hash")
        self.is_bot: bool  = self._get_dict_value(_data, "bot", False)
        self.is_system: bool = self._get_dict_value(_data, "system", False)
        self.mfa_enabled: bool = self._get_dict_value(_data, "mfa_enabled", False)
        self.banner: str = self._get_dict_value(_data, "banner")
        accent_color: int = self._get_dict_value(_data, "accent_color")
        self.accent_color = accent_color.to_bytes().hex() if accent_color else None
        self.locale: str = self._get_dict_value(_data, "locale")
        self.flags: int = self._get_dict_value(_data, "flags")
        self.premium_type: int = self._get_dict_value(_data, "premium_type")
        self.public_flags: int = self._get_dict_value(_data, "public_flags")
        self.avatar_dec = self._get_dict_value(_data, "avatar_decoration_data")

    def _get_dict_value(self, dictionary: dict, key: str, default=None):
        return dictionary.get(key, default)
