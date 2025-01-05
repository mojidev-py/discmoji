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
import datetime
from datetime import datetime
import json
from typing import Optional, Any


class Field:
    """Represents a embed field."""
    def __init__(self,name: str,value: str,inline: bool = False):
        self.name = name
        self.value = value
        self.inline = inline



class Embed:
    """Represents a discord embed."""
    def __init__(self,_data: Optional[dict],title: str = None,embed_type: str = "rich",description: str = None,url: str = None,timestamp: datetime = None,color: int = None):
        self.title: str | None = _data.get("title") if not title else title
        self.type: str | None = _data.get("type") if not embed_type else embed_type
        self.description: str | None = _data.get("description") if not description else description
        self.url: str | None = _data.get("url") if not url else url
        self.timestamp = (datetime.datetime.fromisoformat(_data["timestamp"]) if _data.get("timestamp") else None) if not timestamp else timestamp.isoformat()
        self.color_hex = (hex(_data["color"]) if _data.get("color") else None) if not color else hex(color)
        self.fields = []
        self.footer = None
        """To add a field to this embed, append it to this list."""

    def set_footer(self, text: str = None,icon_url: str = None,proxied_icon_url: str = None):
        """Sets the footer for this embed."""
        self.footer = {
            "text": text,
            "icon_url": icon_url,
            "proxy_icon_url": proxied_icon_url
        }
        for item in (text is None,icon_url is None,proxied_icon_url is None):
            for key in self.footer.keys():
                if item:
                    self.footer.pop(key)
        return self


    def jsonize(self):
        dictized: dict[str, int | str | None | list[Any] | datetime | Any] = {
            "title": self.title,
            "type": self.type,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": int(self.color_hex),
            "fields": [field.__dict__ for field in self.fields],
            "footer": self.footer
        }
        return json.dumps(dictized)

