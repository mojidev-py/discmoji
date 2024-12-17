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
from ..snowflake import Snowflake
from .emoji import Emoji 
from .sticker import Sticker

class GuildPreview:
    """Represents a guild's preview, if bot is not in the guild, requires guild to be discoverable.
    
    ## Attributes
    - id - `discmoji.Snowflake`
      - The guild preview's id.
    - name - `str`
      - The guild's name.
    - icon - `str | None`
      - A formatted CDN link leading to the guild's icon.
    - splash - `str | None`
      - A formatted CDN link leading to the guild's splash.
    - discovery_splash - `str | None`
      - A formatted CDN link leading to the guild's discovery splash.
    - emojis - `list[discmoji.Emoji] | None`
      - A list of the guild's custom emojis.
    - features - `list[str]`
      - A list of all the guild's enabled features.
    - approx_member_count - `int`
      - An approximate of the current amount of members in the guild.
    - approx_presence_count - `int`
      - An approximate of the current amount of presences in the guild.
    - description - `str | None`
      - The guild's description.
    - stickers - `list[discmoji.Sticker]`
      - A list of the guild's custom stickers.
    """
    def __init__(self,dict: dict):
        self.id = Snowflake(dict["id"])
        self.name: str = dict["name"]
        self.icon = f"https://cdn.discordapp.com/icons/{self.id}/{dict["avatar"]}.{"gif" if dict["avatar"].startswith("a_") else "png"}" if dict.get("icon") else None
        self.splash = f"https://cdn.discordapp.com/splashes/{self.id}/{dict["splash"]}.{"gif" if dict["avatar"].startswith("a_") else "png"}" if dict.get("splash") else None
        self.discovery_splash =  f"https://cdn.discordapp.com/discovery-splashes/{self.id}/{dict.get("discovery_splash")}.{"gif" if dict.get("discovery_splash").startswith("a_") else "png"}" if dict.get("discovery_splash") else None
        self.emojis = [Emoji(emoji) for emoji in dict["emojis"]]
        self.features: list[str] = dict["features"]
        self.approx_member_count: int = dict["approximate_member_count"]
        self.approx_presence_count: int = dict["approximate_presence_count"]
        self.description = dict.get("description")
        self.stickers = [Sticker(sticker) for sticker in dict["stickers"]]