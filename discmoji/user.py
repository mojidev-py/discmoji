"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from .snowflake import Snowflake
from ._types import Locales, UserFlags, _flags_parse, _return_nitro_type
from .decoration import AvatarDecoration

class User:
    """Class that represents a discord user.
      ## Attributes
        - id - `discmoji.Snowflake`
          - The id of the User.
        - username - `str`
          - The username of the User.
        - discriminator - `str`
          - The discriminator of the User.
        - global_name - `str | None`
          - The global display name of the user. May not exist.
        - avatar - `str | None`
          - Contains a formatted CDN link that can be used to retrieve the avatar. May not exist.
        - bot - `bool | None`
          - An attribute indicating if the user that this model is representing is an application. May not exist.
        - system - `bool | None`
          - An attribute which indicates whether the user this model is representing is a discord system user/ is part of the urgent message system. (see documentation on User object)
        - mfa - `bool | None`
          - Indicates if the User has multi-factor authentication enabled or not.
        - banner - `str | None`
          - contains a formatted CDN link that can be used to retrieve the banner. May not exist.
        - accent_color - `str | None`
          - contains a hex representation of a color (the "0x" prefix is removed). May be None.
        - locale - `str | None`
          - Indicates the User's chosen language option. May not exist.
        - flags - `list[dict[str,int]] | None`
          - Contains the user's (formatted) flags. May not exist.
        - nitro_type - `Literal["Nitro","Nitro Basic","Nitro Classic"] | None`
          - Contains any one of these literals, depending on the type. May not exist.
        - public_flags - `list[dict[str,int]] | None`
          - Contains the user's (formatted) public flags. May not exist.
        - avatar_decoration - `discmoji.AvatarDecoration`
          - Contains the User's chosen decoration's CDN link.
          """
    def __init__(self,data: dict[str,dict | str | int]):
        self.id: Snowflake = Snowflake(data["id"])
        self.username: str = data["username"]
        self.discriminator: str = data["discriminator"]
        self.global_name: str | None = data.get("global_name")
        self.avatar: str | None = f"https://cdn.discordapp.com/avatar/{self.id}/{data.get("avatar")}.{"gif" if data.get("avatar").startswith("a_") else "png"}" if data.get("avatar") is not None else None
        # avatar is just formatted str for now, as the asset object is made
        self.bot: bool | None = data.get("bot")
        self.system: bool | None = data.get("system")
        self.mfa: bool | None = data.get("mfa_enabled")
        self.banner: str | None = f"https://cdn.discordapp.com/banners/{self.id}/{data.get("banner")}.{"gif" if data.get("banner").startswith("a_") else "png"}" if data.get("banner") is not None else None
        self.accent_color: str | None = hex(data.get("accent_color")).removeprefix("0x") if data.get("accent_color") is not None else None
        self.locale: str | None = Locales.__dict__.get(data.get("locale").upper().replace("-","_")) if data.get("locale") is not None else None
        self.flags = _flags_parse(data.get("flags"))
        self.nitro_type = _return_nitro_type(data.get("premium_type")) 
        self.public_flags = _flags_parse(data.get("flags"))
        self.avatar_decoration = AvatarDecoration(data.get("avatar_decoration_data"))
        
        
        