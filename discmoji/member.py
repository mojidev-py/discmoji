from typing import *





class Member:
    """Represents a discord user."""
    def __init__(self, id: int = 0,
        username: str = "",
        discriminator: str = "#----",
        global_name: str = "anonymous",
        avatar: str = "none",
        mfa_enabled: bool = False,
        banner: str = "none",
        accent_color: int = 000000,	
        locale: str = 000000,	

        premium_type: int = 0	,

        avatar_decoration_data: dict = 0):
        # class attributes
        self.id = id
        self.username= username
        self.discriminator: str =  discriminator	
        self.global_name: str = global_name
        self.avatar: str = avatar
        self.mfa_enabled: bool = mfa_enabled
        self.banner: str = banner
        self.accent_color: int = accent_color	
        self.locale: str = locale
        self.premium_type: int = premium_type	
        self.avatar_decoration_data: dict = avatar_decoration_data