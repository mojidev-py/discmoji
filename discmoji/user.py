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

class User:
    """Class that represents a discord user.
      ## Attributes
        - id - `discmoji.Snowflake`
          - The id of the User.
        - username - `str`
          - The username of the User.
        - discriminator - `str`
          - The discriminator of the User."""
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
        self.banner: str | None = f"https://cdn.discordapp.com/avatar/{self.id}/{data.get("banner")}.{"gif" if data.get("avatar").startswith("a_") else "png"}" if data.get("banner") is not None else None       