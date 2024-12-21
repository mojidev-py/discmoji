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


class Attachment:
    """Represents a discord attachment."""
    def __init__(self,_data: dict):
        self.id = Snowflake(_data["id"])
        self.filename: str = _data["filename"]
        self.title: str = _data["title"]
        self.description: str | None = _data.get("description")
        self.content_type: str | None = _data.get("content_type")
        self.size_in_bytes: int = _data["size"]
        self.url: str = _data["url"]
        self.proxied_url: str = _data["proxy_url"]
        self.img_height: int = _data.get("height")
        self.img_width: int = _data.get("width")
        self.ephemeral: bool | None = _data.get("ephemeral")
        self.duration_in_seconds: int | None = _data.get("duration_secs")
        self.waveform: bytearray | None = _data.get("waveform")
        self.flags = "IS_REMIX" if _data.get("flags") == 1 << 2 else None