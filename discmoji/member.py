from typing import *





class Member:
    """Represents a discord user."""
    def __init__(self):
        id: int = 0
        username: str = ""
        discriminator: str = "#----"	
        global_name: str = "anonymous"
        avatar: str = "none"
        mfa_enabled: bool = False
        banner: str = "none"
        accent_color: int = 000000	
        locale: str = 000000	
        flags: int = 0
        premium_type: int = 0	
        public_flags: int = 0
        avatar_decoration_data: dict = 0